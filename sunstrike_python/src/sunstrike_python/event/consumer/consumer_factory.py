from src.sunstrike_python.config import SunstrikeConfig
from src.sunstrike_python.env import EventConsumerType
from src.sunstrike_python.event.consumer.pulsar_consumer import PulsarConsumer


class EventConsumerFactory:
    def __init__(self):
        pass

    @staticmethod
    def build(config: SunstrikeConfig):
        if config.event_consumer_type == EventConsumerType.PULSAR:
            if not config.pulsar_host:
                raise AttributeError("PULSAR_HOST must be defined.")
            return PulsarConsumer.build(
                host=config.pulsar_host,
                topic=config.topic,
                task_name=config.task_name,
                process_id=config.process_id
            )

