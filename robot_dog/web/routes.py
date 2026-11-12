from __future__ import annotations

from typing import Any


def register_routes(app: Any) -> Any:
    @app.route("/status")
    def status():
        return {"status": "ok"}

    return app
