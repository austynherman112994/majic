from sunstrike_component.component import sunstrike_component
import time

@sunstrike_component()
def print_msg(arg_1, arg_2, kwarg_1_key, kwarg_2_key):
        print(arg_1)
        print(arg_2)
        print(kwarg_1_key)
        print(kwarg_2_key)
print_msg()
