from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Mapping


class ServoController(ABC):
    def __init__(self, config: Mapping[str, Any] | None = None):
        self.config = dict(config or {})

    @abstractmethod
    def initialize(self) -> None:
        """Prepare the servo hardware for active use."""

    @abstractmethod
    def set_angle(self, channel: int, angle: float) -> float:
        """Move a servo to an angle and return the final value."""

    def set_multiple_angles(self, angles: Mapping[int, float]) -> None:
        for channel, angle in angles.items():
            self.set_angle(int(channel), float(angle))

    @abstractmethod
    def disable_outputs(self) -> None:
        """Disable all servo outputs."""

    @abstractmethod
    def close(self) -> None:
        """Free any hardware resources."""


class DistanceSensor(ABC):
    @abstractmethod
    def read_distance(self) -> float:
        """Return the current distance in centimeters."""


class CameraInterface(ABC):
    @abstractmethod
    def capture_frame(self):
        """Return a camera frame or a simulation representation."""


class EmergencyStopInterface(ABC):
    @abstractmethod
    def is_pressed(self) -> bool:
        """Return True when the emergency stop is active."""
