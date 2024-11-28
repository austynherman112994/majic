import pulsar

from sunstrike_python.config import SunstrikeConfig
from sunstrike_python.event.consumer.base_consumer import BaseEventConsumer


class PulsarConsumer(BaseEventConsumer):
    def __init__(self, client, topics: list[str], subscriber):
        self.client = client
        self.topics = topics
        self.subscriber = subscriber
        self.consumer = client.subscribe(topics, subscriber)

        super().__init__()

    @staticmethod
    def build(config: SunstrikeConfig):
        client = pulsar.Client(config.pulsar_host)
        return PulsarConsumer(client, config.topics, config.subscriber)

    def fetch(self):
        return self.consumer.receive()

    def ack(self, msg):
        self.consumer.acknowledge(msg)

    def negative_ack(self, msg):
        self.consumer.negative_acknowledge(msg)

    def close(self):
        self.consumer.close()

