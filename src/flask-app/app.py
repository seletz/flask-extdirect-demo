import logging
from flask import Flask

from log import setup_logging
setup_logging(logging.DEBUG)

import version
import db

# last import
import api

app = Flask(__name__)
app.register_blueprint(api.blueprint, url_prefix="/api/1.0")

if __name__ == "__main__":
    from werkzeug import SharedDataMiddleware
    import os

    db.generate_fake_data()

    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
      '/': os.path.join(os.path.dirname(__file__), 'static')
    })

    # http://werkzeug.pocoo.org/docs/serving/#werkzeug.serving.run_simple
    app.run(debug=True,
            threaded=True,
            use_reloader=True,
            reloader_interval=2)
