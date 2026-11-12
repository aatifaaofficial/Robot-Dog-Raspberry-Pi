from __future__ import annotations

import logging
from typing import Optional

from .config import RobotConfig, load_config
from .control.robot_state import RobotState
from .hardware.pca9685_controller import PCA9685ServoController
from .hardware.servo_controller import SimulationServoController
from .motion.motion_manager import MotionManager


class RobotDogApplication:
    def __init__(self, config_path: str | None = None):
        self.logger = logging.getLogger("robot_dog.application")
        self.config: RobotConfig = load_config(config_path)
        self.config.validate()
        self.robot_state = RobotState(mode=self.config.mode)
        self.servo_controller = None
        self.motion_manager = None

    def startup(self) -> None:
        if self.config.mode == "simulation":
            self.servo_controller = SimulationServoController(self.config)
            self.logger.info("Starting robot in simulation mode")
        else:
            self.servo_controller = PCA9685ServoController(self.config)
            self.logger.info("Starting robot in hardware mode")
        self.servo_controller.initialize()
        self.motion_manager = MotionManager(self.servo_controller, self.config)
        self.robot_state.mode = self.config.mode
        self.robot_state.status = "ready"
        return self

    def run(self) -> None:
        if self.motion_manager is None:
            self.startup()
        self.motion_manager.stand()
        self.robot_state.status = "active"
        self.logger.info("Robot run loop started")

    def shutdown(self) -> None:
        if self.motion_manager is not None:
            self.motion_manager.stop_walking()
        if self.servo_controller is not None:
            self.servo_controller.disable_outputs()
            self.servo_controller.close()
        self.robot_state.status = "stopped"
        self.logger.info("Robot shutdown complete")


def main() -> None:
    app = RobotDogApplication()
    app.startup()
    app.run()


if __name__ == "__main__":
    main()
