from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class PersonDetection:
    label: str
    confidence: float
    center: tuple[int, int]


class PersonDetector:
    def __init__(self, confidence_threshold: float = 0.5):
        self.confidence_threshold = confidence_threshold

    def detect_people(self, frame: Any) -> List[PersonDetection]:
        if frame is None:
            return []
        return [PersonDetection("person", 0.9, (320, 240))]
