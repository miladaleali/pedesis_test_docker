from typing import List

import pedesis.components.symbol_router.controller as router
from pedesis.components.stream_processor.maker import StreamProcessorMaker  # noqa
from pedesis.components.signal_generator.models import DataHandlerAssembly  # noqa
from pedesis.shortcuts import get_source  # noqa
from . import generator as gen  # noqa
from . import optimizer as opt  # noqa
from . import publisher as pub  # noqa
from .settings import settings


# define frequently use variables in this section
_OKX_SRC_PATH = 'pedesis.components.broker.templates.okx'

# =============================================================================
# define source like below
okx = get_source(_OKX_SRC_PATH)

# define data_handler setting like below
data_handler = DataHandlerAssembly(
    data_source=okx.dbid,
    market='future'
)

# define stream processors
gen1 = StreamProcessorMaker(
    processor=gen.SwingShortBollingerBands,
    engine=settings,
    input_=data_handler
)
opt1 = StreamProcessorMaker(processor=opt.HighRiskOptimizer, engine=settings)
pub1 = StreamProcessorMaker(processor=pub.SharpPublisher, engine=settings)


class BaseSymbol(router.SymbolRouter):
    """
    this is a base class for each symbol that will be add in the engine to
    """
    ENGINE_SETTINGS = settings
    ENGINE_PROPERTY = settings.engine_property
    ENGINE_RUN_CONFIGS = {
        'mode': settings.run_mode,
        'start_datetime': settings.backtest_start_datetime,
        'end_datetime': settings.backtest_end_datetime,
    }
    SRL_TIMEFRAMES = settings.srl_timeframes
    SRL_CALCULATORS = settings.installed_srls
    GENERATORS: List[StreamProcessorMaker] = [
        gen1,
    ]
    OPTIMIZERS: List[StreamProcessorMaker] = [
        opt1,
    ]
    PUBLISHERS: List[StreamProcessorMaker] = [
        pub1,
    ]


class BTCUSDT(BaseSymbol):
    pass


class ETHUSDT(BaseSymbol):
    pass


class DOGEUSDT(BaseSymbol):
    pass
