import jinja2

from sunstrike_component.config import SunstrikeConfig


class TemplateEngine:
    def __init__(self):
        self.base_template_parameters = {
            "int": int,
            "float": float,
            "complex": complex,
            "str": str,
            "bool": bool,
            "tuple": tuple,
            "list": list,
            "range": range,
            "set": set,
            "hash": hash,
            "frozenset": frozenset,
            "bytes": bytes,
            "bytearray": bytearray,
        }

    @classmethod
    def build_from_config(cls, config: SunstrikeConfig):
        template_engine = TemplateEngine()
        if config.template_parameters:
            for k, v in config.template_parameters:
                template_engine.add_template_parameter(k, v)
        return template_engine


    def template_arg(self, arg, template_parameters):
        if isinstance(arg, str):
            template = jinja2.Template(arg)
            res_arg = template.render({**self.base_template_parameters, **template_parameters})
        elif isinstance(arg, dict):
            res_arg = {k: self.template_arg(v, template_parameters) for k, v in arg.items()}
        elif isinstance(arg, list) or isinstance(arg, tuple) or isinstance(arg, set):
            res_arg = [self.template_arg(i, template_parameters) for i in arg]
        else:
            res_arg = arg

        return res_arg

    def template_args(self, template_parameters, *args, **kwargs):
        templated_args = self.template_arg(args, template_parameters)
        templated_kwargs = self.template_arg(kwargs, template_parameters)

        return templated_args, templated_kwargs

    def add_template_parameter(self, key, value):
        self.base_template_parameters[key] = value

