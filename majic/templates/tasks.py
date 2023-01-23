from flask import Blueprint

task_blueprint = Blueprint('task_blueprint', __name__)


class Task(func, task_name, *args, **kwargs):

    @task_blueprint.route(f'/tasks/{task_name}', methods=['GET'])
    def task_response():
        data = func(*args, **kwargs)
        return 200, {'message': '', 'status': "SUCCESS", 'job_data': data}
