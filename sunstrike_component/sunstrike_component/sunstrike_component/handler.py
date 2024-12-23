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

    def handle_process(self, func):
        pass

    def handle_sync(self, func):
        pass

    def handle(self, func):
        component_continue = True
        last_check_time = datetime.datetime.now()

        while component_continue:
            try:
                msg = self.event_consumer.fetch(timeout=10000)
                self.event_consumer.ack(msg)
                data = json.loads(msg.data())
                args, kwargs = self.template_engine.template_args(
                    {
                        'sunstrike_msg': data,
                    },
                    *self.function_template.args,
                    **self.function_template.kwargs
                )
                result = func(*args, **kwargs)
                message = json.dumps({
                    "data": result
                }).encode("utf-8")
                self.event_publisher.publish(message)
            except TimeoutError as te:
                logging.debug("Consumer retrieve timed out. Likely due to a lack of messages.")

            delta_time = datetime.datetime.now() - last_check_time
            if delta_time > datetime.timedelta(minutes=1):
                component_continue = True #self.coordinator.component_continue(self.runner_id)
                last_check_time = datetime.datetime.now()

    def _handle(self, topic: str, func):
        futures = []
        if self.concurrency_type == MultiProcessingType.PROCESS:
            with cf.ProcessPoolExecutor(max_workers=self.concurrency) as e:
                futures.append(e.submit(self.run, topic, func))
        elif self.concurrency_type == MultiProcessingType.THREAD:
            with cf.ThreadPoolExecutor(max_workers=self.concurrency) as e:
                futures.append(e.submit(self.run, topic, func))
        else:

            self.run(topic, func)



    def run(self, topic: str, func):
        consumer = EventConsumerFactory.resolve_consumer(self.consu)
        component_continue = True
        last_check_time = datetime.datetime.now()
        logging.error("hello")
        ### TODO Tracing, Metrics, and Logging
        while component_continue:
            try:
                msg = consumer.fetch(timeout=30000)
                consumer.ack(msg)
                args, kwargs = self.template_engine.template_args(
                    {
                        'sunstrike.msg': msg,
                    },
                    *self.function_template.args,
                    **self.function_template.kwargs
                )
                try:
                    result = func(*args, **kwargs)
                    message = {
                        "data": result
                    }
                    self.event_publisher.publish(message)
                except Exception as e:
                    logging.error(e)
                    # Message failed to be processed
                    ## TODO create system error message
                delta_time = datetime.datetime.now() - last_check_time
                if delta_time > datetime.timedelta(minutes=1):
                    component_continue = self.coordinator.component_continue(self.runner_id)
                    last_check_time = datetime.datetime.now()
            except Exception as e:
                logging.error(e)





