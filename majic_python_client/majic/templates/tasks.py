import functools
from flask import Blueprint, request, jsonify

task_blueprint = Blueprint('task_blueprint', __name__)


class Task:
    def __init__(self, function, task_id):
        self.task_id = task_id
        self.connector = connector
        self.function = function

    def task_submit(self):
        parameters = request.get_json()
        result = self.function(**parameters)
        return result, 200

    def task_status(self):
        pass

def task(task_id, connector=None):
    """ Decorator for the class Task

    """
    def _task(function):
        return Task(function, task_id, connector)
    return _task
