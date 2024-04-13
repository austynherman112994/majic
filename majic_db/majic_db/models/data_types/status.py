import enum

class PipelineStatus(enum.Enum):
    active = 0
    paused = 1
    deleted = 3


class PipelineRunStatus(enum.Enum):
    running = 0
    paused = 1
    failed = 3

class TaskRunStatus(enum.Enum):
    scheduled = 0
    on_deck = 1
    queued = 2
    running = 3
    failed = 4
