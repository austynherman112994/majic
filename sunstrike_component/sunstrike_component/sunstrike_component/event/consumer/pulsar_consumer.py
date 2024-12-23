import json
import pulsar

from sunstrike_component.config import SunstrikeConfig
from sunstrike_component.event.consumer.base_consumer import BaseEventConsumer


class PulsarConsumer(BaseEventConsumer):
    def __init__(self, client: pulsar.Client, topics: list[str], subscriber: str):
        self.client = client
        self.topics = topics
        self.subscriber = subscriber
        self.consumer = client.subscribe(topics, subscriber)

        super().__init__()

    @classmethod
    def build_from_config(cls, config: SunstrikeConfig):
        # TODO move to config validation
        if not config.pulsar_host:
            raise AttributeError("SUNSTRIKE_PULSAR_HOST must be defined.")
        if not config.topics:
            raise AttributeError("SUNSTRIKE_INPUT_TOPICS must be defined.")
        if not config.subscriber:
            raise AttributeError("SUNSTRIKE_SUBSCIBER must be defined.")
        return cls.build(config.pulsar_host, config.topics, config.subscriber)

    @classmethod
    def build(cls, host: str, topics: str | list[str], subscriber: str):
        client = pulsar.Client(host)
        return PulsarConsumer(client, topics, subscriber)

    def fetch(self, timeout: int | None = None):
        try:
            return self.consumer.receive(timeout_millis=timeout)
        except pulsar.exceptions.Timeout as pte:
            raise TimeoutError from pte

    def ack(self, msg):
        self.consumer.acknowledge(msg)

    def negative_ack(self, msg):
        self.consumer.negative_acknowledge(msg)

    def close(self):
        self.consumer.close()

