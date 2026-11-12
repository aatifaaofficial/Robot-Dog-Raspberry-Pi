from __future__ import annotations

import os
from typing import Any

try:
    from flask import Flask, render_template
except ImportError:  # pragma: no cover - handled by dependencies
    Flask = None
    render_template = None


def create_app(robot: Any | None = None):
    if Flask is None:
        raise RuntimeError("Flask is required to start the web dashboard.")
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "templates"))

    @app.route("/")
    def index():
        return render_template("index.html", robot=robot)

    return app


def run_web_server(host: str = "0.0.0.0", port: int = 8000, robot: Any | None = None) -> None:
    app = create_app(robot)
    app.run(host=host, port=port, debug=False)
