from sunstrike_component.config import SunstrikeConfig
from sunstrike_component.env import EventStreamingPlatform
from sunstrike_component.event.consumer.pulsar_consumer import PulsarConsumer

from sunstrike_component.event.consumer.base_consumer import BaseEventConsumer


class EventConsumerFactory:
    def __init__(self, config: SunstrikeConfig):
        self.config = config

    @classmethod
    def build_from_config(cls, config: SunstrikeConfig):
        consumer = cls.resolve_consumer(config.event_consumer_type)
        return consumer.build_from_config(config)

    @classmethod
    def resolve_consumer(cls, event_consumer_type: EventStreamingPlatform) -> BaseEventConsumer:
        if event_consumer_type == EventStreamingPlatform.PULSAR:
            return PulsarConsumer
        else:
            raise NotImplementedError(f"Consumer type {event_consumer_type} not implemented")
