import pulsar

from sunstrike_python.config import SunstrikeConfig


class PulsarPublisher:
    def __init__(self, client, topic):
        self.client = client
        self.producer = self.client.create_producer(topic)

        super().__init__()

    @staticmethod
    def build(config: SunstrikeConfig):
        client = pulsar(config.pulsar_host)
        return PulsarPublisher(client, config.output_topic)

    def publish(self, message):
        self.producer.send(message)

    def close(self):
        self.client.close()
