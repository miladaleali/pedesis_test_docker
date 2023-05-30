from pedesis.conf.global_settings import BaseStationSettings


class StationSettings(BaseStationSettings):
    installed_engines: list[str] = []  # populate this with engine names.

    installed_brokers: list[str] = [
        'pedesis.components.broker.templates.okx',
    ]

    installed_data_sources: dict[str, str] = {
        'okx': 'pedesis.components.broker.templates.okx',
    }


settings = StationSettings()
