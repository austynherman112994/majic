import json
import concurrent.futures as cf
import datetime
import logging


from sunstrike_component.config import SunstrikeConfig
from sunstrike_component.coordinator import Coordinator
from sunstrike_component.template import TemplateEngine
from sunstrike_component.types import MultiProcessingType, FunctionTemplate
from sunstrike_component.event.consumer.base_consumer import BaseEventConsumer
from sunstrike_component.event.publisher.base_publisher import BaseEventPublisher



from sunstrike_component.event.consumer.consumer_factory import EventConsumerFactory

from sunstrike_component.template import TemplateInterface


class Handler:
    def __init__(
            self,
            runner_id: str,
            event_consumer: BaseEventConsumer,
            event_publisher: BaseEventPublisher,
            coordinator: Coordinator,
            template_engine: TemplateEngine,
            function_template: FunctionTemplate,
            concurrency: int,
            concurrency_type: MultiProcessingType,
            timeout: int
    ):
        self.runner_id = runner_id
        self.event_consumer = event_consumer
        self.event_publisher = event_publisher
        self.coordinator = coordinator
        self.concurrency = concurrency
        self.concurrency_type = concurrency_type
        self.template_engine = template_engine
        self.function_template = function_template
        self.timeout = timeout

    @classmethod
    def build(
            cls,
            event_consumer: BaseEventConsumer,
            event_publisher: BaseEventPublisher,
            coordinator: Coordinator,
            template_engine: TemplateEngine,
            config: SunstrikeConfig
    ):

        return Handler(
            runner_id=config.runner_id,
            event_consumer=event_consumer,
            event_publisher=event_publisher,
            coordinator=coordinator,
            template_engine=template_engine,
            function_template=config.function_template,
            concurrency=config.concurrency,
            concurrency_type=config.concurrency_type,
            timeout=config.timeout
        )

    def handle(self, func):
        component_continue = True
        last_check_time = datetime.datetime.now()

        while component_continue:
            msg = self.consume_message(func)
            if msg:
                args, kwargs = self.template_params(msg)
                result = func(*args, **kwargs)
                self.publish_results(result)

            delta_time = datetime.datetime.now() - last_check_time
            if delta_time > datetime.timedelta(minutes=1):
                component_continue = True # self.coordinator.component_continue(self.runner_id)
                last_check_time = datetime.datetime.now()

    def consume_message(self, func):
        try:
            msg = self.event_consumer.fetch(timeout=10000)
            self.event_consumer.ack(msg)
            return msg
        except TimeoutError as te:
            logging.debug("Consumer retrieve timed out. Likely due to a lack of messages.")
        return None

    def template_params(self, msg):
        args, kwargs = self.template_engine.template_args(
            {
                'sunstrike_msg': msg,
                'sunstrike_input': json.loads(msg.data())
            },
            *self.function_template.args,
            **self.function_template.kwargs
        )
        return args, kwargs

    def publish_results(self, results: dict):
        msg_data = json.dumps(results).encode('utf-8')
        self.event_publisher.publish(msg_data)




