import os
from dotenv import load_dotenv
load_dotenv()

from pedesis.conf.global_settings import BaseStationSettings, DataBaseSetting


class StationSettings(BaseStationSettings):
    installed_engines: list[str] = [
        'multi_long_triple_ema_scalp',
        'scalp_short_macd',
        'swing_long_bollinger_bands',
        'swing_short_bollinger_bands',
    ]  # populate this with engine names.

    installed_brokers: list[str] = [
        'pedesis.components.broker.templates.okx',
    ]

    installed_databases: dict = {
        'default': DataBaseSetting(
            controller='pedesis.db.controller.LiveDataBase', 
            url=os.environ['NEON_DATABASE_URL']
        )
    }

    installed_data_sources: dict[str, str] = {
        'okx': 'pedesis.components.broker.templates.okx',
    }


settings = StationSettings()
