import os
import enum

class MultiProcessingType(enum.Enum):
    THREAD = "THREAD"
    PROCESS = "PROCESS"
    NONE = "NONE"

    @classmethod
    def _missing_(cls, value):
        return cls.NONE

class EventConsumerType(enum.Enum):
    PULSAR = "PULSAR"
    NONE = "NONE"

    @classmethod
    def _missing_(cls, value):
        return cls.NONE


SUNSTRIKE_COMPONENT_CONCURRENCY = os.environ.get("SUNSTRIKE_COMPONENT_CONCURRENCY")
SUNSTRIKE_COMPONENT_MULTIPROCESSING_TYPE = MultiProcessingType(
    os.environ.get("SUNSTRIKE_COMPONENT_MULTIPROCESSING_TYPE"))
SUNSTRIKE_EVENT_CONSUMER_TYPE = EventConsumerType(
    os.environ.get("SUNSTRIKE_EVENT_CONSUMER_TYPE")
)

SUNSTRIKE_PULSAR_HOST = 'pulsar://pulsar-proxy.sunstrike.svc.cluster.local:6650'
SUNSTRIKE_TOPICS = ''
