import enum
from dataclasses import dataclass


class MultiProcessingType(enum.Enum):
    THREAD = "THREAD"
    PROCESS = "PROCESS"
    NONE = "NONE"

    @classmethod
    def _missing_(cls, value):
        return cls.NONE

class EventStreamingPlatform(enum.Enum):
    PULSAR = "PULSAR"
    NONE = "NONE"

    @classmethod
    def _missing_(cls, value):
        return cls.NONE

class CacheType(enum.Enum):
    REDIS = "REDIS"
    NONE = "NONE"

    @classmethod
    def _missing_(cls, value):
        return cls.NONE

@dataclass
class FunctionTemplate:
    args: list | tuple
    kwargs: dict
