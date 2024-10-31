

class BaseEventQueue:
    def __init__(self):
        pass

    def publish(self, key):
        raise NotImplemented("Cache get_obj must be overridden")
