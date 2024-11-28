from sunstrike_python.cache.base_cache import BaseCache


class DummyCache(BaseCache):
    __cache = {}
    def __init__(self):
        super().__init__()

    def get_runner_state(self, key):
        raise NotImplemented("Cache get_str must be overridden")

    def set_runner_state(self, key):
        raise NotImplemented("Cache get_obj must be overridden")

    def get_str(self, key):
        return DummyCache.__cache[key]

    def get_obj(self, key):
        return DummyCache.__cache[key]

    def set_str(self, key, val):
        DummyCache.__cache[key] = val
        return True

    def set_obj(self, key: str, val: dict):
        DummyCache.__cache[key] = val
        return True

