from __future__ import annotations

from robot_dog.hardware.camera import Camera


camera = Camera({"source": 0})
print(camera.capture_frame())
