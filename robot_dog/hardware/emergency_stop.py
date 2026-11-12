from __future__ import annotations

from robot_dog.hardware.interfaces import EmergencyStopInterface


class EmergencyStop(EmergencyStopInterface):
    def __init__(self, enabled: bool = True):
        self.enabled = enabled
        self._pressed = False

    def set_pressed(self, pressed: bool) -> None:
        self._pressed = bool(pressed)

    def is_pressed(self) -> bool:
        return self.enabled and self._pressed
