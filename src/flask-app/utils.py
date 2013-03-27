import flask
import functools

def returns_json(f):
    """returns_json(function) -> function

    Returns a function which JSON serializes the passed function's
    output and returns a request with correct mimetype set.
    """
    @functools.wraps(f)
    def wrapper(*args, **kw):
        result = flask.json.dumps(f(*args, **kw),
                indent=None if flask.request.is_xhr else 2)
        return flask.current_app.response_class(result,
                mimetype="application/json")

    return wrapper

def returns_js(f):
    """returns_js(function) -> function

    Returns a response mime type `application/javascript`
    """
    @functools.wraps(f)
    def wrapper(*args, **kw):
        result = f(*args, **kw)
        return flask.current_app.response_class(result,
                mimetype="application/javascript")

    return wrapper
