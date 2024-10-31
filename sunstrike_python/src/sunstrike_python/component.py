from src.sunstrike_python.config import SunstrikeConfig
from src.sunstrike_python.consumer import Consumer

class _SunstrikeComponent(object):
    def __init__(self, func, config: SunstrikeConfig):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.consume_messages()

    @staticmethod
    def build(func, config: SunstrikeConfig):

        return _SunstrikeComponent(func, config)

    def consume_messages(self, *args, **kwargs):
        for msg in SunstrikeConsumer.consume():
            result = self.func(msg, *args, **kwargs)

def SunstrikeComponent(func, config: SunstrikeConfig | None = None):
    if not config:
        config = SunstrikeConfig.from_env()
    def wrapper(func):
        return _SunstrikeComponent(func, config)
    return wrapper



