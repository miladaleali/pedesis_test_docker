from pedesis.components.pubsub.tasks import publish_message
from pedesis.components.signal_generator.models import IncomeGeneratorMsgType

if __name__ == '__main__':
    gen_id = int(input('give generator id: '))
    gen_mult = int(input('give quality adjuster id: '))
    gen_channel = f"SPInside::generator@{gen_id}"
    publish_message(
        channel=gen_channel,
        message={
            'msg': IncomeGeneratorMsgType.DebugSendSignal,
            'data': {
                'signal_adjuster': gen_mult
            }

        }
    )
