import redis

from src.sunstrike_python.cache.base_cache import BaseCache


class RedisCache(BaseCache):
    def __init__(self):
        self.client = redis.Redis(host='localhost', port=6379, decode_responses=True)

        super().__init__()

    def get_str(self, key):
        return self.client.get(key)

    def get_obj(self, key):
        return self.client.hgetall(key)

    def set_str(self, key, val):
        return self.client.set(key, val)

    def set_obj(self, key: str, val: dict):
        return self.client.hset(key, mapping=val)
