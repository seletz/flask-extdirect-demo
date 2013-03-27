from flask import Flask
app = Flask(__name__)


if __name__ == "__main__":
    from werkzeug import SharedDataMiddleware
    import os

    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
      '/': os.path.join(os.path.dirname(__file__), 'static')
    })

    # http://werkzeug.pocoo.org/docs/serving/#werkzeug.serving.run_simple
    app.run(debug=True,
            threaded=True,
            use_reloader=True,
            reloader_interval=2)

