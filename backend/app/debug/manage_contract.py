import os
import typer
from celery.contrib.abortable import AbortableAsyncResult

from pedesis.shortcuts import get_model, get_current_cache
from pedesis.components.user.maker import get_user
from pedesis.components.contract.controller import ContractManager

app = typer.Typer()
cont_model = get_model('ContractModel')
ub_model = get_model('UserBrokerModel')
broker_model = get_model('Broker')
pos_model = get_model('OpenPositionModel')


def convert_period_to_timestamp(period: int) -> float:
    from pedesis.utils import make_dtime_timestamp
    now = make_dtime_timestamp()
    day_timestamp = 24 * 60 * 60
    return now + (period * day_timestamp)


def create_contract(len_contract: int = 1):
    from pedesis.utils import make_dtime_timestamp

    username = 'miladaleali'
    password = '123456'
    broker_name = 'okx'
    amount = 40_000 if len_contract == 1 else 60_000
    risk_pct = 50
    period = 360

    try:
        user = get_user(username_or_email=username, password=password)
    except Exception as e:
        typer.echo(e, err=True)
        return
    broker_id = broker_model.get('id', name=broker_name)
    if not broker_id:
        broker_id = broker_model(name=broker_name).save().id

    register_time = make_dtime_timestamp()
    period_timestamp = convert_period_to_timestamp(period)

    if len_contract > 2:
        typer.echo("contract len is greater than 2.")
        return

    else:
        amt = amount if len_contract == 1 else (0.6 * amount)
        for _ in range(len_contract):
            cont_model(
                user_id=user.id,
                broker_id=broker_id,
                time_registered=register_time,
                expire_timestamp=period_timestamp,
                total_margin=amt,
                risk_tolerance_pct=risk_pct,
            ).save()
            amt = amount - amt

    typer.echo(f'{len_contract} Contract created!!')


def create_user_brokers(len_contract: int = 1):
    username = 'miladaleali'
    password = '123456'
    user = get_user(username, password)
    broker = 'okx'
    broker_id = broker_model.get('id', name=broker)
    if not broker_id:
        broker_id = broker_model(name=broker).save().id
    cont_break = len_contract
    cont_ids = list(map(int, cont_model.all(in_df=True).id.values))
    for i in range(4):
        if len_contract > 1:
            if cont_break:
                cont_break -= 1
            else:
                cont_break = len_contract
                cont_ids.pop(0)
        params = {
            'user': user,
            'broker_name': broker,
            'contract_id': cont_ids[0]
        }
        params["api_key"] = os.environ.get(f"DEBUG_BROKER_API_KEY{i}", None)
        params["api_secret"] = os.environ.get(
            f"DEBUG_BROKER_SECRET_KEY{i}", None)
        params["api_password"] = os.environ.get(
            f"DEBUG_BROKER_PASSPHRASE{i}", None)
        params["api_type"] = os.environ.get(f"DEBUG_API_TYPE{i}", None)
        name = params["api_name"] = os.environ.get(f"DEBUG_API_NAME{i}", None)
        if ub_model.get(user_id=user.id, broker_id=broker_id, api_name=params['api_name']):
            typer.echo(f"UserBroker {name} already exists!")
            continue
        ub_model.from_user(
            **params
        )
        typer.echo(f"UserBroker {name} created!")


def send_contract_to_station():
    from pedesis.station.messenger import send_station_msg, MSG

    contract_ids = list(map(int, cont_model.all(in_df=True).id.values))
    for id_ in contract_ids:
        send_station_msg(
            msg_type=MSG.ContractCreated,
            msg={'contract_id': id_},
        )
        typer.echo(f'Contract {id_} added to running station')


def stop_contract_task(contract_id: int) -> None:
    task_id = ContractManager.get_task_id(contract_id)
    AbortableAsyncResult(task_id).abort()
    typer.echo(f"Abort Contract {contract_id}.")


def clean_cache():
    cache = get_current_cache()
    with cache._cache as c:
        keys = list(map(lambda x: x.decode(), c.keys("*Contract:*")))
        if keys:
            c.delete(*keys)
    typer.echo('Clean cache keys.')


def clean_beat():
    pattern = '*EngineClusterTask::revise_performance*'
    cache = get_current_cache()
    with cache._cache as c:
        keys = list(map(lambda x: x.decode(), c.keys(pattern)))
        if keys:
            c.delete(keys)


def delete_contracts():
    contracts = cont_model.all(all_=True, scalars=True)
    for cont in contracts:
        id_ = cont.id
        stop_contract_task(id_)
        positions = pos_model.get_open_positions_ids(id_)
        for pos in positions:
            pos = pos_model.get(id=pos).get_pydantic_model()
            AbortableAsyncResult(pos.task_id).abort()
            typer.echo(f"Abort position {pos.id}.")
        cont.delete(id=id_)
        typer.echo(f'Delete Contract {id_} From DB.')


def delete_gps():
    gp_model = get_model('GenericPositionModel')
    gps = gp_model.all(all_=True, scalars=True)
    for gp in gps:
        try:
            AbortableAsyncResult(gp.task_id).abort()
        except Exception:
            pass
        typer.echo(f"Abort GP {gp.id} task and task id was {gp.task_id}.")
        gp.delete(id=gp.id)


@app.command()
def init(len_contract: int) -> None:
    typer.echo('Initialize contracts...')
    len_contract = int(len_contract)
    create_contract(len_contract)
    create_user_brokers(len_contract)
    send_contract_to_station()
    typer.echo('Initializing is done...')


@app.command()
def delete() -> None:
    typer.echo('Start Deleting...')
    delete_contracts()
    delete_gps()
    clean_beat()
    clean_cache()
    typer.echo('Deleting done.')


if __name__ == '__main__':
    app()
