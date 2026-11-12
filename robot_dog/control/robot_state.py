from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class RobotState:
    mode: str = "simulation"
    status: str = "initialized"
    walking: bool = False
    battery_level: float = 100.0
    last_command: str = "stand"
    metadata: Dict[str, Any] = field(default_factory=dict)

    def update(self, **kwargs: Any) -> "RobotState":
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self

    def snapshot(self) -> Dict[str, Any]:
        return {
            "mode": self.mode,
            "status": self.status,
            "walking": self.walking,
            "battery_level": self.battery_level,
            "last_command": self.last_command,
            "metadata": self.metadata,
        }
