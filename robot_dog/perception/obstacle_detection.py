from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class ObstacleReport:
    distance_cm: float
    clear: bool

    def as_dict(self) -> Dict[str, Any]:
        return {"distance_cm": self.distance_cm, "clear": self.clear}


class ObstacleDetector:
    def __init__(self, minimum_distance_cm: float = 20.0):
        self.minimum_distance_cm = minimum_distance_cm

    def detect(self, distance_cm: float) -> ObstacleReport:
        return ObstacleReport(distance_cm=distance_cm, clear=distance_cm > self.minimum_distance_cm)
