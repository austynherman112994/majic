from sunstrike_python.config import SunstrikeConfig
from sunstrike_python.env import EventStreamingPlatform
from sunstrike_python.event.consumer.pulsar_consumer import PulsarConsumer


class EventConsumerFactory:
    def __init__(self):
        pass

    @classmethod
    def build(cls, config: SunstrikeConfig):
        consumers = []
        if config.event_consumer_type == EventStreamingPlatform.PULSAR:
            if not config.pulsar_host:
                raise AttributeError("PULSAR_HOST must be defined.")
            consumers.append(
                PulsarConsumer.build(config=config)
            )
        return consumers

