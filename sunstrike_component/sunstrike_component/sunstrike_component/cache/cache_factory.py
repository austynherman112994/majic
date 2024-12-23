from sunstrike_component.cache.base_cache import BaseCache
from sunstrike_component.cache.redis_cache import RedisCache
from sunstrike_component.config import SunstrikeConfig
from sunstrike_component.types import CacheType


class CacheFactory:
    def __init__(self):
        pass

    @classmethod
    def build_from_config(cls, config: SunstrikeConfig) -> BaseCache:
        if config.cache_type == CacheType.REDIS:
            cache = RedisCache.build(config)
        else:
            raise NotImplementedError("Cache configuration is required")

        return cache
