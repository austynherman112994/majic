import redis

from sunstrike_python.cache.base_cache import BaseCache
from sunstrike_python.config import SunstrikeConfig


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

    def set_runner_active_task_runs(self, runner_id, num_active_task_runs):
        self.client.set(f"{runner_id}_active_runs", num_active_task_runs)

    def set_task_runner_list_runner_id(self, task_id, runner_id):
        self.client.rpush(f"{task_id}_runner_list", runner_id)

    def remove_task_list_runner_id(self, task_id, runner_id):
        self.client.lrem(f"{task_id}_runner_list", 0, runner_id)



