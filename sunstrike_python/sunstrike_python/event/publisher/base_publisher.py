

class BaseEventPublisher:
    def __init__(self):
        pass

    def publish(self, key):
        raise NotImplemented("Event publisher publish must be overridden")

    def close(self, key):
        raise NotImplemented("Event publisher close must be overridden")
