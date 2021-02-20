"""Flask App."""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from .nav import nav
from .frontend import frontend
from flask_debug import Debug

app = Flask(
    __name__,
)
# We use Flask-Appconfig here, but this is not a requirement
AppConfig(app)
Debug(app)
Bootstrap(app)
nav.init_app(app)
app.register_blueprint(frontend)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
