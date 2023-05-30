from pedesis.shortcuts import (
    get_settings,
    get_data_handler,
)
from pedesis.components.data.models import DataType
from pedesis.logger import get_logger

if __name__ == '__main__':
    logger = get_logger()

    settings = get_settings()
    data_types = [
        DataType.Future,
        DataType.Spot,
        DataType.FutureDelivery,
    ]

    for src in settings.installed_data_sources.values():
        for data_type in data_types:
            try:
                get_data_handler(
                    source=src,
                    data_type=data_type
                )
            except KeyError as e:
                logger.info(f"-- load data source index -- while adding {data_type} to {src} this error happe:\n\t{e}")
