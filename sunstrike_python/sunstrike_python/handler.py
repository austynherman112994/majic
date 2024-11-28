import concurrent.futures as cf
from sunstrike_python.config import SunstrikeConfig
from sunstrike_python.coordinator import Coordinator
from sunstrike_python.template import TemplateEngine
from sunstrike_python.types import MultiProcessingType, FunctionTemplate
from sunstrike_python.event.consumer.base_consumer import BaseEventConsumer
from sunstrike_python.event.publisher.base_publisher import BaseEventPublisher

import logging


class Handler:
    def __init__(
            self,
            runner_id: str,
            event_consumers: list[BaseEventConsumer],
            event_publisher: BaseEventPublisher,
            coordinator: Coordinator,
            template_engine: TemplateEngine,
            function_template: FunctionTemplate,
            concurrency: int,
            concurrency_type: MultiProcessingType
    ):
        self.runner_id = runner_id
        self.event_consumers = event_consumers
        self.event_publisher = event_publisher
        self.coordinator = coordinator
        self.concurrency = concurrency
        self.concurrency_type = concurrency_type
        self.template_engine = template_engine
        self.function_template = function_template

    @classmethod
    def build(
            cls,
            event_consumers: list[BaseEventConsumer],
            event_publisher: BaseEventPublisher,
            coordinator: Coordinator,
            template_engine: TemplateEngine,
            config: SunstrikeConfig
    ):

        return Handler(
            config.runner_id,
            event_consumers,
            event_publisher,
            coordinator,
            template_engine,
            config.function_template,
            config.concurrency,
            config.concurrency_type
        )


    def process(self, func):
        futures = []
        with cf.ProcessPoolExecutor(max_workers=len(self.event_consumers)) as executor:
            for consumer in self.event_consumers:
                futures.append(
                    executor.submit(
                        self._process,
                        consumer,
                        func
                    )
                )
        return [future.result() for future in futures]

    def _process(self, consumer, func):
        futures = []
        while self.coordinator.component_continue(self.runner_id) and len(futures) <= self.concurrency:
            msg = consumer.fetch()
            args, kwargs = self.template_engine.template_args(
                {
                    'sunstrike.msg': msg,
                },
                *self.function_template.args,
                **self.function_template.kwargs
            )
            try:
                if self.concurrency_type == MultiProcessingType.PROCESS:
                    with cf.ProcessPoolExecutor(max_workers=self.concurrency) as e:
                        pass
                elif self.concurrency_type == MultiProcessingType.THREAD:
                    with cf.ThreadPoolExecutor(max_workers=self.concurrency) as e:

                else:
                    func(*args, **kwargs)
                consumer.ack(msg)
            except Exception as e:
                logging.error(e)
                # Message failed to be processed
                consumer.negative_ack(msg)


        consumer.close()

    def run_function(self, func, run_config, message, *args, **kwargs):

        func()






