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

def fetch_all():
    global data
    return {"items": data.values(),
            "count": len(data.keys())}

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
    return fetch_all()

@blueprint.route("/data/<int:id>", methods=["GET"])
@utils.returns_json
@blueprint.extdirect(klass="NXDB")
def db_fetch(id):
    if id is None:
        return fetch_all()
    try:
        return data[id]
    except KeyError:
        flask.abort(404)

@blueprint.route("/data", methods=["PUT"])
@utils.returns_json
@blueprint.extdirect(klass="NXDB")
def db_create(data):
    out = create(data)
    return out

@blueprint.route("/data/<int:id>", methods=["POST"])
@utils.returns_json
@blueprint.extdirect(klass="NXDB")
def db_update(items):
    if isinstance(items, dict):
        items = [items]

    out = []
    for item in items:
        out.append(update(item["id"], item))

    return out

@blueprint.route("/data/<int:id>", methods=["DELETE"])
@utils.returns_json
@blueprint.extdirect(klass="NXDB")
def db_delete(items):
    if isinstance(items, dict):
        items = [items]

    out = []
    for item in items:
        out.append(delete(item["id"]))

    return out


# vim: set ft=python ts=4 sw=4 expandtab :
