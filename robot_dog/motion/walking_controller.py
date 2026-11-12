from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class WalkingController:
    step_height: float = 18.0
    step_length: float = 18.0
    cycle_duration: float = 1.2
    walking: bool = False

    def walk_forward(self, speed: float = 1.0) -> Dict[str, Any]:
        self.walking = True
        return {"command": "walk_forward", "speed": float(speed), "status": "running"}

    def walk_backward(self, speed: float = 1.0) -> Dict[str, Any]:
        self.walking = True
        return {"command": "walk_backward", "speed": float(speed), "status": "running"}

    def turn_left(self, speed: float = 1.0) -> Dict[str, Any]:
        self.walking = True
        return {"command": "turn_left", "speed": float(speed), "status": "running"}

    def turn_right(self, speed: float = 1.0) -> Dict[str, Any]:
        self.walking = True
        return {"command": "turn_right", "speed": float(speed), "status": "running"}

    def stop(self) -> Dict[str, Any]:
        self.walking = False
        return {"command": "stop", "status": "stopped"}
