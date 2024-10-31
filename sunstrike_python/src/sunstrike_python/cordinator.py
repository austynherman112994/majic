import redis

from src.sunstrike_python.cache.base_cache import BaseCache


class Cordinator:
    def __init__(self, cache: BaseCache):
        self.cache = cache

    @classmethod
    def build(cls):
        pass

    def component_continue(self, process_id: str, task_id: str):
        return True


