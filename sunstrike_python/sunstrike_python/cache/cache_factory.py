from sunstrike_python.cache.base_cache import BaseCache
from sunstrike_python.cache.redis_cache import RedisCache
from sunstrike_python.config import SunstrikeConfig
from sunstrike_python import CacheType


class CacheFactory:
    def __init__(self):
        pass

    @classmethod
    def build(cls, config: SunstrikeConfig) -> BaseCache:
        cache = None
        if config.cache_type == CacheType.REDIS:
            cache = RedisCache.build(config)
        else:
            raise NotImplemented("Cache configuration is required")

        return cache
