import pulsar

from sunstrike_component.config import SunstrikeConfig


class PulsarPublisher:
    def __init__(self, client, topic):
        self.client = client
        self.producer = self.client.create_producer(topic)

        super().__init__()

    @classmethod
    def build_from_config(cls, config: SunstrikeConfig):
        return cls.build(config.pulsar_host, config.output_topic)

    @classmethod
    def build(cls, host, topic):
        client = pulsar.Client(host)
        return PulsarPublisher(client, topic)

    def publish(self, message):
        self.producer.send(message)

    def close(self):
        self.client.close()
