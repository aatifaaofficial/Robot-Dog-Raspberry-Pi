from __future__ import annotations

from typing import Any, Mapping

from robot_dog.hardware.interfaces import ServoController
from robot_dog.utils.validators import clamp_angle, validate_channel

try:  # pragma: no cover - exercised when hardware is available
    import board
    import busio
    from adafruit_pca9685 import PCA9685
except ImportError:  # pragma: no cover - fallback for simulation
    board = None
    busio = None
    PCA9685 = None


class PCA9685ServoController(ServoController):
    def __init__(self, config: Mapping[str, Any] | None = None):
        super().__init__(config)
        self._controller = None
        raw_config = config.as_dict()["robot"] if hasattr(config, "as_dict") else (dict(config or {}) if isinstance(config, dict) else {})
        servo_config = raw_config.get("servo", {}) if isinstance(raw_config, dict) else {}
        self._channels = list(servo_config.get("channels", list(range(12))))
        self.min_angle = float(servo_config.get("min_angle", -90.0))
        self.max_angle = float(servo_config.get("max_angle", 90.0))

    def initialize(self) -> None:
        if PCA9685 is None:
            raise RuntimeError(
                "PCA9685 support requires the adafruit-circuitpython-pca9685 package. "
                "The robot is running in simulation mode unless you install this library."
            )
        i2c = busio.I2C(board.SCL, board.SDA)
        self._controller = PCA9685(i2c)
        self._controller.frequency = 60

    def set_angle(self, channel: int, angle: float) -> float:
        channel = validate_channel(channel, self._channels)
        value = clamp_angle(float(angle), self.min_angle, self.max_angle)
        if self._controller is None:
            raise RuntimeError("Servo controller has not been initialized.")
        # Duty cycle usage is approximate for compatibility with a wide range of servos.
        duty = (value + 90.0) / 180.0
        self._controller.channels[channel].duty_cycle = int(duty * 65535)
        return value

    def disable_outputs(self) -> None:
        if self._controller is not None:
            for channel in self._channels:
                self._controller.channels[channel].duty_cycle = 0

    def close(self) -> None:
        if self._controller is not None:
            self.disable_outputs()
            self._controller = None
