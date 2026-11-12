from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Sequence, Tuple


@dataclass
class DetectedObject:
    label: str
    confidence: float
    bounding_box: Tuple[int, int, int, int]

    def as_dict(self) -> Dict[str, Any]:
        return {
            "label": self.label,
            "confidence": self.confidence,
            "bounding_box": list(self.bounding_box),
        }


class ObjectDetector:
    def __init__(self, confidence_threshold: float = 0.5):
        self.confidence_threshold = confidence_threshold

    def detect(self, frame: Any) -> List[DetectedObject]:
        if frame is None:
            return []
        return [DetectedObject("object", 0.8, (0, 0, 10, 10))]
