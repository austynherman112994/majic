from sunstrike_python.config import SunstrikeConfig
from sunstrike_python.event.publisher.pulsar_publisher import PulsarPublisher
from sunstrike_python.types import EventStreamingPlatform


class EventPublisherFactory:
    def __init__(self):
        pass

    @classmethod
    def build(cls, config: SunstrikeConfig):
        producer = None
        if config.event_publisher_type == EventStreamingPlatform.PULSAR:
            if not config.pulsar_host:
                raise AttributeError("PULSAR_HOST must be defined.")
            producer = PulsarPublisher.build(config=config)

        return producer

