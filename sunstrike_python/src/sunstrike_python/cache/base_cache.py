

class BaseCache:
    def __init__(self):
        pass

    def get_str(self, key):
        raise NotImplemented("Cache get_str must be overridden")

    def get_obj(self, key):
        raise NotImplemented("Cache get_obj must be overridden")

    def set_str(self, key, val):
        raise NotImplemented("Cache set_str must be overridden")

    def set_obj(self, key: str, val: dict):
        raise NotImplemented("Cache set_obj must be overridden")
