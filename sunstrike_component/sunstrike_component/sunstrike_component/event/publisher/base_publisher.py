from sunstrike_component.config import SunstrikeConfig


class BaseEventPublisher:
    def __init__(self):
        pass

    def publish(self, message):
        raise NotImplementedError("Event publisher publish must be overridden")

    def close(self):
        raise NotImplementedError("Event publisher close must be overridden")

    @classmethod
    def build_from_config(cls, config: SunstrikeConfig):
        raise NotImplementedError("Event publisher close must be overridden")
