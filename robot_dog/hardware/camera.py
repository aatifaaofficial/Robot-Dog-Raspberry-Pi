from __future__ import annotations

from typing import Any

from robot_dog.hardware.interfaces import CameraInterface


class Camera(CameraInterface):
    def __init__(self, config: dict[str, Any] | None = None):
        self.config = config or {}
        self.source = self.config.get("source", 0)

    def capture_frame(self):
        return {"source": self.source, "shape": (480, 640, 3), "simulated": True}
