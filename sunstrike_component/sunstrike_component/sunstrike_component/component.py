from sunstrike_component.cache.cache_factory import CacheFactory
from sunstrike_component.config import SunstrikeConfig
from sunstrike_component.handler import Handler
from sunstrike_component.coordinator import Coordinator
from sunstrike_component.event.consumer.consumer_factory import EventConsumerFactory
from sunstrike_component.event.publisher.publisher_factory import EventPublisherFactory
from sunstrike_component.template import TemplateEngine


class SunstrikeComponent(object):
    def __init__(self, func, runner_id, handler):
        self.func = func
        self.runner_id = runner_id
        self.handler = handler

    def handle(self, func):
        self.handler.handle(func)

    @classmethod
    def build(cls, func, config: SunstrikeConfig):
        template_engine = TemplateEngine.build_from_config(config)
        cache = CacheFactory.build_from_config(config)
        event_consumer = EventConsumerFactory.build_from_config(config)
        coordinator = Coordinator.build(cache)

        event_publisher = EventPublisherFactory.build_from_config(config)

        handler = Handler.build(
            event_consumer,
            event_publisher,
            coordinator,
            template_engine,
            config)

        return SunstrikeComponent(func, config.runner_id, handler)


def sunstrike_component(config: SunstrikeConfig | None = None):
    if not config:
        config = SunstrikeConfig.from_env()

    def sunstrike_decorator(func):
        sunstrike = SunstrikeComponent.build(func, config)

        def wrapper():
            sunstrike.handle(func)
        return wrapper
    return sunstrike_decorator




