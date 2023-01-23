import functools
from flask import Blueprint

task_blueprint = Blueprint('task_blueprint', __name__)


def task(task_id):
    def task_wrapper(func):
        @functools.wraps(func)
        @task_blueprint.route(f'/tasks/{task_id}', methods=['GET'])
        def task_response(*args, **kwargs):
            data = func(*args, **kwargs)
            return 200, {'message': '', 'status': "SUCCESS", 'job_data': data}

        return task_response
    return task_wrapper
