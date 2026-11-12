from __future__ import annotations

from typing import Any, Dict, Mapping

from robot_dog.motion.balance_controller import BalanceController
from robot_dog.motion.kinematics import LegGeometry, stand_pose
from robot_dog.motion.walking_controller import WalkingController


class MotionManager:
    def __init__(self, servo_controller: Any | None = None, config: Mapping[str, Any] | None = None):
        self.servo_controller = servo_controller
        if hasattr(config, "as_dict"):
            self.config = config.as_dict().get("robot", {})
        elif isinstance(config, dict):
            self.config = config
        else:
            self.config = {}
        motion_config = self.config.get("motion", {}) if isinstance(self.config, dict) else {}
        self.walking_controller = WalkingController(
            step_height=motion_config.get("step_height", 18.0),
            step_length=motion_config.get("step_length", 18.0),
            cycle_duration=motion_config.get("gait_cycle_duration", 1.2),
        )
        self.balance_controller = BalanceController(self.config)
        self.geometry = LegGeometry()

    def stand(self) -> Dict[str, Any]:
        pose = stand_pose(self.geometry)
        if self.servo_controller is not None:
            self.servo_controller.set_multiple_angles({0: 0.0, 1: 0.0, 2: 0.0})
        return {"motion": "stand", "pose": pose, "status": "ready"}

    def sit(self) -> Dict[str, Any]:
        return {"motion": "sit", "status": "ready"}

    def lie_down(self) -> Dict[str, Any]:
        return {"motion": "lie_down", "status": "ready"}

    def walk_forward(self, speed: float = 1.0) -> Dict[str, Any]:
        return self.walking_controller.walk_forward(speed)

    def walk_backward(self, speed: float = 1.0) -> Dict[str, Any]:
        return self.walking_controller.walk_backward(speed)

    def turn_left(self, speed: float = 1.0) -> Dict[str, Any]:
        return self.walking_controller.turn_left(speed)

    def turn_right(self, speed: float = 1.0) -> Dict[str, Any]:
        return self.walking_controller.turn_right(speed)

    def stop_walking(self) -> Dict[str, Any]:
        return self.walking_controller.stop()

    def return_to_neutral(self) -> Dict[str, Any]:
        return {"motion": "return_to_neutral", "status": "ready"}
