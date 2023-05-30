from pedesis.components.signal_publisher.templates import base

from .publisher_settings import (
    SharpPublisherSettings,
)


class SharpPublisher(base.Publisher):
    SETTINGS = SharpPublisherSettings
