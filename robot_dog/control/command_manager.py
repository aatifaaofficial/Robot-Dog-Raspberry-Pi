from __future__ import annotations

from typing import Any, Dict


class CommandManager:
    def __init__(self, motion_manager: Any | None = None):
        self.motion_manager = motion_manager

    def handle_command(self, command: str) -> Dict[str, Any]:
        key = command.strip().lower()
        mapping = {
            "stand": (self._stand, {}),
            "sit": (self._sit, {}),
            "lie down": (self._lie_down, {}),
            "walk forward": (self._walk_forward, {}),
            "walk backward": (self._walk_backward, {}),
            "turn left": (self._turn_left, {}),
            "turn right": (self._turn_right, {}),
            "stop": (self._stop, {}),
        }
        if key not in mapping:
            return {"command": command, "status": "unknown"}
        func, kwargs = mapping[key]
        return func(**kwargs)

    def _stand(self) -> Dict[str, Any]:
        if self.motion_manager is not None:
            return self.motion_manager.stand()
        return {"command": "stand", "status": "ok"}

    def _sit(self) -> Dict[str, Any]:
        if self.motion_manager is not None:
            return self.motion_manager.sit()
        return {"command": "sit", "status": "ok"}

    def _lie_down(self) -> Dict[str, Any]:
        if self.motion_manager is not None:
            return self.motion_manager.lie_down()
        return {"command": "lie_down", "status": "ok"}

    def _walk_forward(self) -> Dict[str, Any]:
        if self.motion_manager is not None:
            return self.motion_manager.walk_forward()
        return {"command": "walk_forward", "status": "ok"}

    def _walk_backward(self) -> Dict[str, Any]:
        if self.motion_manager is not None:
            return self.motion_manager.walk_backward()
        return {"command": "walk_backward", "status": "ok"}

    def _turn_left(self) -> Dict[str, Any]:
        if self.motion_manager is not None:
            return self.motion_manager.turn_left()
        return {"command": "turn_left", "status": "ok"}

    def _turn_right(self) -> Dict[str, Any]:
        if self.motion_manager is not None:
            return self.motion_manager.turn_right()
        return {"command": "turn_right", "status": "ok"}

    def _stop(self) -> Dict[str, Any]:
        if self.motion_manager is not None:
            return self.motion_manager.stop_walking()
        return {"command": "stop", "status": "ok"}
