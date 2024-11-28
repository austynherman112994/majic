from sunstrike_python.cache.base_cache import BaseCache

class Coordinator:
    def __init__(self, cache: BaseCache):
        self.cache = cache

    @classmethod
    def build(cls, cache: BaseCache):
        return Coordinator(cache)

    def component_continue(self, runner_id: str) -> bool:
        return self.cache.get_runner_shutdown(runner_id)


