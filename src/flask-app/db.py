import flask
import logging
import utils

from api import blueprint

logger = logging.getLogger("db")

def counter(start=0):
    current = start
    while True:
        yield current
        current = current + 1

id_generator = counter()

data = {}

def create(row):
    global data
    id = id_generator.next()
    data[id] = row
    data[id]["id"] = id
    return data[id]

def update(id, row):
    global data
    if id not in data:
        raise KeyError(id)
    data[id] = row
    data[id]["id"] = id
    return data[id]

def delete(id):
    global data
    if id not in data:
        raise KeyError(id)
    return data.pop(id)

def generate_fake_data(n=10):
    global data
    for k in range(n):
        create({
            "name": "Fred %d" % k,
            "number": k
            })

@blueprint.route("/data", methods=["GET"])
@utils.returns_json
@blueprint.extdirect(klass="NXDB")
def db_fetch_all():
    return data

@blueprint.route("/data/<int:id>", methods=["GET"])
@utils.returns_json
@blueprint.extdirect(klass="NXDB")
def db_fetch(id):
    try:
        return data[id]
    except KeyError:
        flask.abort(404)

@blueprint.route("/data", methods=["PUT"])
@utils.returns_json
@blueprint.extdirect(klass="NXDB")
def db_create():
    return create(flask.request.json)

@blueprint.route("/data/<int:id>", methods=["POST"])
@utils.returns_json
@blueprint.extdirect(klass="NXDB")
def db_update(id):
    return update(id, flask.request.json)

@blueprint.route("/data/<int:id>", methods=["DELETE"])
@utils.returns_json
@blueprint.extdirect(klass="NXDB")
def db_delete(id):
    return delete(id)


# vim: set ft=python ts=4 sw=4 expandtab :
