from sunstrike_component.cache.base_cache import BaseCache


class DummyCache(BaseCache):
    __cache = {}
    def __init__(self):
        super().__init__()

    def get_runner_shutdown(self, runner_id: str) -> bool:
        return self.__cache.get(f"{runner_id}_shutdown").lower() == "true"
