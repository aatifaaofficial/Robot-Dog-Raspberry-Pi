from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class GaitParameters:
    step_height: float = 18.0
    step_length: float = 18.0
    cycle_duration: float = 1.2
    lift_ratio: float = 0.5

    def as_dict(self) -> Dict[str, float]:
        return {
            "step_height": self.step_height,
            "step_length": self.step_length,
            "cycle_duration": self.cycle_duration,
            "lift_ratio": self.lift_ratio,
        }


def generate_walk_cycle(step_height: float = 18.0, step_length: float = 18.0, cycle_duration: float = 1.2) -> List[Dict[str, Any]]:
    cycle = []
    for phase in range(4):
        cycle.append(
            {
                "phase": phase,
                "label": "lift" if phase in {0, 2} else "stance",
                "step_height": step_height,
                "step_length": step_length,
                "duration": cycle_duration / 4.0,
            }
        )
    return cycle
