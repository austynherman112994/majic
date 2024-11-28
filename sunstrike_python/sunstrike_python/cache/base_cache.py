

class BaseCache:
    def __init__(self):
        pass

    def get_runner_shutdown(self, runner_id: str) -> bool:
        raise NotImplemented("Cache get_str must be overridden")

    def set_runner_active_task_runs(self, runner_id, num_active_task_runs):
        raise NotImplemented("Cache get_str must be overridden")

    def update_task_runner_list(self, task_id, runner_id):
        raise NotImplemented("Cache get_str must be overridden")
