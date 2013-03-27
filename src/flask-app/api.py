import flask
import logging
import extdirect

logger = logging.getLogger("api")

blueprint = extdirect.ExtDirectBlueprint("api", __name__, )

# vim: set ft=python ts=4 sw=4 expandtab :
