import flask
import logging
import utils
import extdirect

logger = logging.getLogger("api")

blueprint = extdirect.ExtDirectBlueprint("api", __name__, )

@blueprint.route("/version")
@utils.returns_json
@blueprint.extdirect(klass="NXGateway")
def version():
    logger.debug("GET: version")
    return {
        "version": 0.1,
        "build":   1,
        "date":    "2013-03-27" }
