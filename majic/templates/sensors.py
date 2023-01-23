from flask import Blueprint

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')


def task(func, task_name, *args, **kwargs):

    @task_blueprint.route(f'/tasks/{task_name}', methods=['GET'])
    def task_response():
        data = func(*args, **kwargs)
        return 200, data



