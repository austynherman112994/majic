from sunstrike_component.config import SunstrikeConfig


class BaseEventConsumer:
    def __init__(self):
        pass

    def fetch(self, timeout: int | None = None):
        raise NotImplementedError("Event consumer fetch must be overridden")

    def ack(self, msg):
        raise NotImplementedError("Event consumer ack must be overridden")

    def negative_ack(self, msg):
        raise NotImplementedError("Event consumer negative ack must be overridden")

    def close(self):
        raise NotImplementedError("Event consumer close must be overridden")

    @classmethod
    def build_from_config(cls, config: SunstrikeConfig):
        raise NotImplementedError("Event publisher close must be overridden")
