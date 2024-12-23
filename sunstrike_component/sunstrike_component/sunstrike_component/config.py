import os

from sunstrike_component.env import SUNSTRIKE_EVENT_CONSUMER_TYPE, \
    SUNSTRIKE_PULSAR_HOST, SUNSTRIKE_INPUT_TOPICS, SUNSTRIKE_CACHE_TYPE, SUNSTRIKE_REDIS_PORT, \
    SUNSTRIKE_REDIS_HOST, SUNSTRIKE_COMPONENT_MULTIPROCESSING_TYPE, \
    SUNSTRIKE_COMPONENT_CONCURRENCY, SUNSTRIKE_EVENT_PRODUCER_TYPE, SUNSTRIKE_OUTPUT_TOPIC, SUNSTRIKE_SUBSCRIBER, \
    SUNSTRIKE_FUNCTION_TEMPLATE, SUNSTRIKE_FUNCTION_TIMEOUT, SUNSTRIKE_RUNNER_ID
from sunstrike_component.types import CacheType, MultiProcessingType, EventStreamingPlatform, FunctionTemplate


class SunstrikeConfig:
    def __init__(
        self,
        runner_id: str,
        event_consumer_type: EventStreamingPlatform,
        event_publisher_type: EventStreamingPlatform,
        topics: list[str],
        subscriber: str,
        output_topic: str,
        pulsar_host: str | None,
        cache_type: CacheType,
        redis_host: str,
        redis_port: str | int,
        concurrency: int,
        concurrency_type: MultiProcessingType,
        timeout: int,
        function_template: FunctionTemplate,
        template_parameters: dict | None
    ):
        self.runner_id = runner_id
        self.event_consumer_type = event_consumer_type
        self.event_publisher_type = event_publisher_type
        self.topics = topics
        self.subscriber = subscriber
        self.output_topic = output_topic
        self.pulsar_host = pulsar_host
        self.cache_type = cache_type
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.concurrency = concurrency
        self.concurrency_type = concurrency_type
        self.function_template = function_template
        self.template_parameters = template_parameters
        self.timeout = timeout


    @staticmethod
    def from_env():
        return SunstrikeConfig(
            runner_id=SUNSTRIKE_RUNNER_ID,
            event_consumer_type=SUNSTRIKE_EVENT_CONSUMER_TYPE,
            event_publisher_type=SUNSTRIKE_EVENT_PRODUCER_TYPE,
            topics=SUNSTRIKE_INPUT_TOPICS,
            subscriber=SUNSTRIKE_SUBSCRIBER,
            output_topic=SUNSTRIKE_OUTPUT_TOPIC,
            pulsar_host=SUNSTRIKE_PULSAR_HOST,
            cache_type=SUNSTRIKE_CACHE_TYPE,
            redis_host=SUNSTRIKE_REDIS_HOST,
            redis_port=SUNSTRIKE_REDIS_PORT,
            concurrency=SUNSTRIKE_COMPONENT_CONCURRENCY,
            concurrency_type=SUNSTRIKE_COMPONENT_MULTIPROCESSING_TYPE,
            timeout=SUNSTRIKE_FUNCTION_TIMEOUT,
            function_template=SUNSTRIKE_FUNCTION_TEMPLATE,
            template_parameters=None,
        )
