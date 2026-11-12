from __future__ import annotations

from robot_dog.hardware.servo_controller import SimulationServoController


controller = SimulationServoController({"servo": {"channels": [0, 1, 2], "min_angle": -90, "max_angle": 90}})
controller.initialize()
print(controller.set_angle(1, 45))
controller.disable_outputs()
controller.close()
