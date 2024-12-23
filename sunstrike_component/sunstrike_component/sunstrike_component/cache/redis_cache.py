import redis

from sunstrike_component.cache.base_cache import BaseCache
from sunstrike_component.config import SunstrikeConfig


class RedisCache(BaseCache):
    def __init__(self, client: redis.Redis):
        self.client = client

        super().__init__()

    @classmethod
    def build(cls, config: SunstrikeConfig):
        client = redis.Redis(
            host=config.redis_host,
            port=config.redis_port,
            decode_responses=True
        )
        return RedisCache(client)

    def get_runner_shutdown(self, runner_id: str) -> bool:
        return self.client.get(f"{runner_id}_shutdown").lower() == "true"




