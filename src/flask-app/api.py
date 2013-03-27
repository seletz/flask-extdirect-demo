import flask
import logging
import utils
import extdirect

logger = logging.getLogger("api")

blueprint = extdirect.ExtDirectBlueprint("api", __name__, )

# @blueprint.route("/version") ->
@blueprint.extdirect(klass="NXGateway")
# @utils.returns_json
def version():
    logger.debug("GET: version")
    return {
        "version": 0.1,
        "build":   1,
        "date":    "2013-03-27" }
