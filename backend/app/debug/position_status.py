import typer

from pedesis.shortcuts import get_model

app = typer.Typer()
pos_model = get_model('OpenPositionModel')

@app.command()
def fetchall():
    typer.echo(pos_model.all(in_df=True))

def get_generic_orders_msg(orders: list) -> str:
    main_msg = ""
    end_ = "-=" * 20
    for order in orders:
        msg = f"\n\tUID: {order.uid}\n\tMargin: {order.margin}\n\tType: {order.type}\n\tPrice: {order.price}\n\tLeverage: {order.leverage}\n\tBuy Side: {order.buy_side}\n\tParams: {order.params}\n\t{end_}"
        main_msg += msg
    return main_msg

def get_orders_msg(orders: list) -> str:
    end_ = "-=" * 20
    for order in orders:
        msg = f"\n\tGeneric UID: {order.generic_order.uid}\n\t"
        ord_dict = order.dict(
            exclude={
                'generic_order',
                'created_order',
                'fetched_order'
            }
        )
        nxt_ln = '\n\t'
        _msg = list(map(lambda x: f"{x[0]}: {x[1]}", ord_dict.items()))
        __msg = nxt_ln.join(_msg)
        msg += __msg
        if (co := order.created_order):
            msg += f"\n\tCreate Order:\n\t\tEndpoint: {co.endpoint}\n\t\tRequest: {co.request}\n\t\tResponse: {co.response}"
        if (fo := order.fetched_order):
            msg += f"\n\tFetch Order:\n\t\tEndpoint: {fo.endpoint}\n\t\tRequest: {fo.request}\n\t\tResponse: {fo.response}"
        msg += end_
    return msg

@app.command()
def fetchone(position_id: int):
    typer.secho(f'Fetching Position {position_id}', fg='green')
    pos = pos_model.get(id=position_id).get_pydantic_model()

    typer.secho('Contract Info:', fg=typer.colors.YELLOW)
    typer.echo(
        f"\tContract ID: {pos.contract_dbid}\n\tContract Total Margin: {pos.contract_total_margin}\n\tContract Total Risk: {pos.contract_total_risk}\n\tContract Cache UID: {pos.contract_cache_uid}"
    )

    typer.secho('Position General Info:', fg=typer.colors.YELLOW)
    typer.echo(
        f"\tSymbol: {pos.symbol}\n\tMargin Portion: {pos.margin_portion}\n\tLeverage: {pos.leverage}\n\tRisk: {pos.risk}\n\tTotal Enter Amount Filled: {pos.total_enter_amount_filled}\n\tTotal Exit Amount Filled: {pos.total_exit_amount_filled}\n\tSent: {pos.is_sent}\n\tOpen: {pos.is_opened}\n\tClosed: {pos.is_closed}\n\tPnL: {pos.pnl}\n\t"
    )

    typer.secho('Position Checkpoint Info:', fg=typer.colors.YELLOW)
    typer.echo(
        f"\tStage: {pos.checkpoint_stage}\n\tLevel: {pos.checkpoint_level}\n\tLast Checkpoint ID: {pos.last_checkpoint_id}"
    )

    typer.secho('Position Enter Orders:', fg=typer.colors.YELLOW)
    typer.secho('Main:', fg=typer.colors.RED)
    mains = pos.total_orders.main.orders
    typer.echo(f"{get_generic_orders_msg(mains)}")

    if pos.generic_position.has_dca:
        typer.secho('DCA:', fg=typer.colors.RED)
        dcas = pos.total_orders.dca.orders
        typer.echo(f"{get_generic_orders_msg(dcas)}")
    else:
        typer.secho('DCA order not found!', fg=typer.colors.RED)

    typer.secho('Position Exit Orders:', fg=typer.colors.YELLOW)
    typer.secho('tp:', fg=typer.colors.RED)
    tps = pos.total_orders.tp.orders
    typer.echo(f"{get_generic_orders_msg(tps)}")

    typer.secho('sl:', fg=typer.colors.RED)
    sls = pos.total_orders.sl.orders
    typer.echo(f"{get_generic_orders_msg(sls)}")

    typer.secho('Position Released Orders:', fg=typer.colors.YELLOW)
    if (exist_lines := pos.released_orders.exist_lines()):
        for line, order_line in exist_lines.items():
            typer.secho(f'{line.upper()} Line:', fg=typer.colors.RED)
            typer.echo(get_orders_msg(order_line.orders))
    else:
        typer.secho('Position Has No Released Orders!', fg=typer.colors.BRIGHT_RED)

    typer.secho('Position Done Orders:', fg=typer.colors.YELLOW)
    if (exist_lines := pos.done_orders.exist_lines()):
        for line, order_line in exist_lines.items():
            typer.secho(f'{line.upper()} Line:', fg=typer.colors.RED)
            typer.echo(get_orders_msg(order_line.orders))
    else:
        typer.secho('Position Has No Done Orders!', fg=typer.colors.BRIGHT_RED)

if __name__ == '__main__':
    app()
