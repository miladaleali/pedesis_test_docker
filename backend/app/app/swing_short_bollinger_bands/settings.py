from datetime import datetime

from pedesis.components.signal_engine import models
from pedesis.conf.global_settings import EngineSettings

settings = EngineSettings(
    name='swing_short_bollinger_bands',
    run_mode='live',
    folder_name='swing_short_bollinger_bands',
    mode=models.EngineMode.Scalp,
    native_broker='pedesis.components.broker.templates.okx',
    market=models.DataType.Future,
    backtest_start_datetime='2022-06-01 00:00:00',
    back_populate_start_datetime=datetime(2022, 6, 1).timestamp(),
    installed_data_sources={
        'okx': 'pedesis.components.broker.templates.okx',
    },
    installed_srls=[
        'pedesis.components.srl_calculator.calculators.williams_fractal'
    ],
    srl_timeframes=[
        '5m',
        '15m',
        '30m',
        '1h',
        '2h',
        '4h',
        '6h',
        '12h',
        '1d',
        '3d',
        '1w',
        '1M',
    ],
    installed_symbols=[
        'BTCUSDT',
        'ETHUSDT',
        'DOGEUSDT'
    ]
)
