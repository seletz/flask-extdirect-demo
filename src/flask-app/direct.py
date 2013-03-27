import flask
import utils

direct = flask.Blueprint("api", __name__)

@direct.route("/version")
@utils.returns_json
def version():
    return {
        "version": 0.1,
        "build":   1,
        "date":    "2013-03-27" }
