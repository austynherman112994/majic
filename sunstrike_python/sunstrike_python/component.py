from sunstrike_python.cache.cache_factory import CacheFactory
from sunstrike_python.config import SunstrikeConfig
from sunstrike_python.handler import Handler
from sunstrike_python.coordinator import Coordinator
from sunstrike_python.event.consumer.consumer_factory import EventConsumerFactory
from sunstrike_python.event.publisher.producer_factory import EventPublisherFactory
from sunstrike_python.template import TemplateEngine


class _SunstrikeComponent(object):
    def __init__(self, func, runner_id, consumer):
        self.func = func
        self.runner_id = runner_id
        self.consumer = consumer

    def __call__(self, *args, **kwargs):
        self.consumer.consume(self, self.func, *args, **kwargs)

    @classmethod
    def build(cls, func, config: SunstrikeConfig):
        template_engine = TemplateEngine.build(config)
        cache = CacheFactory.build(config)
        event_consumers = EventConsumerFactory.build(config)
        coordinator = Coordinator.build(cache)

        event_publisher = EventPublisherFactory.build(config)

        consumer = Handler.build(
            event_consumers,
            event_publisher,
            coordinator,
            template_engine,
            config)

        return _SunstrikeComponent(func, config.runner_id, consumer)


def sunstrike_component(func, config: SunstrikeConfig | None = None):
    if not config:
        config = SunstrikeConfig.from_env()
    def wrapper():
        return _SunstrikeComponent.build(func, config)
    return wrapper



