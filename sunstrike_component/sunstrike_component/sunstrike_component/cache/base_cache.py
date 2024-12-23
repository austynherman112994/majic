

class BaseCache:
    def __init__(self):
        pass

    def get_runner_shutdown(self, runner_id: str) -> bool:
        raise NotImplemented("Cache get_runner_shutdown must be overridden")

