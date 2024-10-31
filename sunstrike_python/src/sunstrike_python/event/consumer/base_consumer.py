from src.sunstrike_python.config import SunstrikeConfig


class BaseEventConsumer:
    def __init__(self):
        pass

    def fetch(self, key):
        raise NotImplemented("Event consumer fetch must be overridden")

    def ack(self, msg):
        raise NotImplemented("Event consumer ack must be overridden")

    def negative_ack(self, msg):
        raise NotImplemented("Event consumer negative ack must be overridden")
