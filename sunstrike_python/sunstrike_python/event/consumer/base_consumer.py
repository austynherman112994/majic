class BaseEventConsumer:
    def __init__(self):
        pass

    def fetch(self):
        raise NotImplemented("Event consumer fetch must be overridden")

    def ack(self, msg):
        raise NotImplemented("Event consumer ack must be overridden")

    def negative_ack(self, msg):
        raise NotImplemented("Event consumer negative ack must be overridden")

    def close(self, msg):
        raise NotImplemented("Event consumer close must be overridden")
