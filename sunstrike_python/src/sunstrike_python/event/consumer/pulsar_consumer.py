import pulsar

from src.sunstrike_python.event.consumer.base_consumer import BaseEventConsumer


class PulsarConsumer(BaseEventConsumer):
    def __init__(self, client, topic, task_name, process_id):
        self.consumer = client
        self.task_name = task_name
        self.topic = topic
        self.subscription = task_name
        self.consumer = client.subscribe(topic, self.subscription)
        self.process_id = process_id


        super().__init__()

    @staticmethod
    def build(host, topic, task_name, process_id):
        client = pulsar.Client(host)
        return PulsarConsumer(client, topic, task_name, process_id)

    def fetch(self, key):
        return self.consumer.receive()

    def ack(self, msg):
        self.consumer.acknowledge(msg)

    def negative_ack(self, msg):
        self.consumer.negative_acknowledge(msg)

    def close(self):
        self.client.close()

