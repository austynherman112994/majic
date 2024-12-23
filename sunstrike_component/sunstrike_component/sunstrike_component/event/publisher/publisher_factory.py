from sunstrike_component.config import SunstrikeConfig
from sunstrike_component.event.publisher.pulsar_publisher import PulsarPublisher
from sunstrike_component.types import EventStreamingPlatform

from sunstrike_component.event.publisher.base_publisher import BaseEventPublisher


class EventPublisherFactory:
    def __init__(self):
        pass

    @classmethod
    def build_from_config(cls, config: SunstrikeConfig):
        publisher = cls.resolve_publisher(config.event_publisher_type)
        return publisher.build_from_config(config)

    @classmethod
    def resolve_publisher(cls, event_publisher_type: EventStreamingPlatform) -> BaseEventPublisher:
        if event_publisher_type == EventStreamingPlatform.PULSAR:
            return PulsarPublisher
        else:
            raise NotImplementedError(f"Publisher type {event_publisher_type} not implemented")
