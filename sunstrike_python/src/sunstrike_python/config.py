from mimetypes import inited

from src.sunstrike_python.env import SUNSTRIKE_EVENT_CONSUMER_TYPE, EventConsumerType, \
    SUNSTRIKE_PULSAR_HOST, SUNSTRIKE_TOPICS


class SunstrikeConfig:
    def __init__(
        self,
        event_consumer_type: EventConsumerTypeEnum,

        pulsar_host: str | None
    ):
        self.event_consumer_type = event_consumer_type
        pass

    @staticmethod
    def from_env():

        return SunstrikeConfig(
            event_consumer_type=SUNSTRIKE_EVENT_CONSUMER_TYPE,
            topics=SUNSTRIKE_TOPICS,
            pulsar_host=SUNSTRIKE_PULSAR_HOST
        )
