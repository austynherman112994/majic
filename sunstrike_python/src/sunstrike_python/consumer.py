
from src.sunstrike_python.config import SunstrikeConfig
from src.sunstrike_python.cordinator import Cordinator
from src.sunstrike_python.event.consumer.base_consumer import BaseEventConsumer


class Consumer:
    def __init__(
            self,
            event_consumer: BaseEventConsumer,
            cordinator: Cordinator,
    ):
        self.event_consumer = event_consumer
        self.cordinator = cordinator


    def build(self, config: SunstrikeConfig):
        pass

    def consume(self):
        consumer = self.client.subscribe('my-topic', 'my-subscription')

        while self.cordinator.component_continue():
            msg = consumer.receive()
            try:
                print("Received message '{}' id='{}'".format(msg.data(), msg.message_id()))
                # Acknowledge successful processing of the message
                consumer.acknowledge(msg)
            except Exception:
                # Message failed to be processed
                consumer.negative_acknowledge(msg)

        client.close()


