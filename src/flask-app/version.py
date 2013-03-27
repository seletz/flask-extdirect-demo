import flask
import logging
import utils

from api import blueprint

logger = logging.getLogger("version")

@blueprint.route("/version")
@utils.returns_json
@blueprint.extdirect(klass="NXGateway")
def version():
    logger.debug("GET: version")
    return {
        "version": 0.1,
        "build":   1,
        "date":    "2013-03-27" }

# vim: set ft=python ts=4 sw=4 expandtab :
