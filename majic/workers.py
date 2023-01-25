
""" Flask app initialization.

This module initializes the instance of a flask app and
registers the routes and error handlers.

"""


import flask

from majic import templates




class Workers:
    def __init__(self, default_tasks=True, default_sensors=True):
        self.app = flask.Flask(__name__)
        self.task_blueprint = Blueprint('task_blueprint', __name__)
        self.sensor_blueprint = Blueprint('sensor_blueprint', __name__)
        self.app.register_blueprint(blueprint)


    def add_task(self, task):
        pass

    def add_sensor(self, sensor):
        pass

    def start_workers(self):



app = flask.Flask(__name__)

# Register route blueprints
app.register_blueprint(templates.tasks.task_blueprint)

# Register error handlers
# app.register_blueprint(handlers.error_blueprint)

# This will only run in a local env where
# this file is called directly.
# The runtime will be a WSGI server when not local.
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8001)
