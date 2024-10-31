import json
import flask

import logging
from sunstrike_db.controllers.pipeline import PipelineController
from sunstrike_db.engine import DbEngine

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

pipeline_blueprint = flask.Blueprint("pipeline_blueprint", __name__, url_prefix="/pipeline")

pipeline_controller = PipelineController(DbEngine.instance())

@pipeline_blueprint.route("/", methods=["GET"])
def get_pipelines():
    pipelines = pipeline_controller.read_all()
    return json.dumps(pipelines), 200

@pipeline_blueprint.route("/{pipeline_id}", methods=["GET"])
def get_pipeline():
    pipeline = pipeline_controller.read()
    return json.dumps(pipeline), 200


@pipeline_blueprint.route("/{pipeline_id}", methods=["POST"])
def create_pipelines():
    pipeline = pipeline_controller.read()
    return json.dumps(pipeline), 200
