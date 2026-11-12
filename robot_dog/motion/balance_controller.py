from __future__ import annotations

from typing import Any, Dict


class BalanceController:
    def __init__(self, config: dict[str, Any] | None = None):
        self.config = config or {}

    def stabilize(self, target_angles: Dict[str, Dict[str, float]]) -> Dict[str, Dict[str, float]]:
        stabilized = {}
        for name, angles in target_angles.items():
            stabilized[name] = {key: float(value) for key, value in angles.items()}
        return stabilized
