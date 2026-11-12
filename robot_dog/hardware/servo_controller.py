from __future__ import annotations

from typing import Any, Mapping

from robot_dog.hardware.interfaces import ServoController
from robot_dog.utils.validators import clamp_angle, validate_channel


class SimulationServoController(ServoController):
    def __init__(self, config: Mapping[str, Any] | None = None):
        super().__init__(config)
        raw_config = config.as_dict()["robot"] if hasattr(config, "as_dict") else (dict(config or {}) if isinstance(config, dict) else {})
        servo_config = raw_config.get("servo", {}) if isinstance(raw_config, dict) else {}
        self.channels = list(servo_config.get("channels", list(range(12))))
        self.min_angle = float(servo_config.get("min_angle", -90.0))
        self.max_angle = float(servo_config.get("max_angle", 90.0))
        self._angles = {int(channel): 0.0 for channel in self.channels}
        self._initialized = False

    def initialize(self) -> None:
        self._initialized = True

    def set_angle(self, channel: int, angle: float) -> float:
        channel = validate_channel(channel, self.channels)
        safe_angle = clamp_angle(float(angle), self.min_angle, self.max_angle)
        self._angles[channel] = safe_angle
        return safe_angle

    def set_multiple_angles(self, angles: Mapping[int, float]) -> None:
        for channel, angle in angles.items():
            self.set_angle(int(channel), float(angle))

    def disable_outputs(self) -> None:
        self._angles = {channel: 0.0 for channel in self.channels}

    def close(self) -> None:
        self._initialized = False

    @property
    def angles(self):
        return dict(self._angles)
