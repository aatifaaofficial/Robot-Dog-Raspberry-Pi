from __future__ import annotations

from robot_dog.hardware.interfaces import DistanceSensor


class UltrasonicDistanceSensor(DistanceSensor):
    def __init__(self, config=None, simulated: bool = True):
        self.config = config or {}
        self.simulated = simulated

    def read_distance(self) -> float:
        if self.simulated:
            return 45.0
        return 45.0
