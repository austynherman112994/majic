"""Main module."""
from flask import Flask
# from rollbar.routes.score import score_blueprint
from routes.pipeline import pipeline_blueprint
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)


app.register_blueprint(pipeline_blueprint)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
