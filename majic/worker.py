
""" Flask app initialization.

This module initializes the instance of a flask app and
registers the routes and error handlers.

"""


import flask

from majic import templates

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
