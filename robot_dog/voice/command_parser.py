from __future__ import annotations

from typing import Any, Dict


class CommandParser:
    @staticmethod
    def parse(command: str) -> Dict[str, Any]:
        text = (command or "").strip().lower()
        mapping = {
            "stand": {"command": "stand"},
            "sit": {"command": "sit"},
            "lie down": {"command": "lie_down"},
            "walk forward": {"command": "walk_forward"},
            "walk backward": {"command": "walk_backward"},
            "turn left": {"command": "turn_left"},
            "turn right": {"command": "turn_right"},
            "stop": {"command": "stop"},
        }
        return mapping.get(text, {"command": "unknown", "raw": command})
