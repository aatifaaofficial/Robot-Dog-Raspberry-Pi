from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, Mapping

try:
    import yaml
except ImportError as exc:  # pragma: no cover - handled at runtime
    raise RuntimeError("PyYAML is required to load robot configuration.") from exc

DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[1] / "config" / "robot.yaml"


@dataclass
class RobotConfig:
    mode: str = "simulation"
    robot_name: str = "Rover"
    safe_mode: bool = True
    emergency_stop_enabled: bool = True
    hardware: Dict[str, Any] = field(default_factory=dict)
    motion: Dict[str, Any] = field(default_factory=dict)
    servo: Dict[str, Any] = field(default_factory=dict)
    camera: Dict[str, Any] = field(default_factory=dict)
    safety: Dict[str, Any] = field(default_factory=dict)
    web: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_file(cls, path: str | Path | None = None) -> "RobotConfig":
        config_path = Path(path) if path is not None else DEFAULT_CONFIG_PATH
        if not config_path.exists():
            config_path.parent.mkdir(parents=True, exist_ok=True)
            config_path.write_text(_default_yaml_text(), encoding="utf-8")
        with config_path.open("r", encoding="utf-8") as handle:
            loaded = yaml.safe_load(handle) or {}
        payload = build_default_config()
        payload.update(loaded)
        return cls.from_mapping(payload)

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "RobotConfig":
        robot = data.get("robot", data)
        hardware = robot.get("hardware", {})
        motion = robot.get("motion", {})
        servo = robot.get("servo", {})
        camera = robot.get("camera", {})
        safety = robot.get("safety", {})
        web = robot.get("web", {})
        return cls(
            mode=str(robot.get("mode", "simulation")).lower(),
            robot_name=str(robot.get("name", robot.get("robot_name", "Rover"))),
            safe_mode=bool(robot.get("safe_mode", True)),
            emergency_stop_enabled=bool(robot.get("emergency_stop_enabled", True)),
            hardware=dict(hardware),
            motion=dict(motion),
            servo=dict(servo),
            camera=dict(camera),
            safety=dict(safety),
            web=dict(web),
        )

    def get(self, *keys: str, default: Any = None) -> Any:
        current: Any = self.__dict__
        for key in keys:
            if not isinstance(current, Mapping) or key not in current:
                return default
            current = current[key]
        return current

    def as_dict(self) -> Dict[str, Any]:
        return {
            "robot": {
                "name": self.robot_name,
                "mode": self.mode,
                "safe_mode": self.safe_mode,
                "emergency_stop_enabled": self.emergency_stop_enabled,
                "hardware": self.hardware,
                "motion": self.motion,
                "servo": self.servo,
                "camera": self.camera,
                "safety": self.safety,
                "web": self.web,
            }
        }

    def validate(self) -> None:
        if self.mode not in {"simulation", "hardware"}:
            raise ValueError("Robot mode must be either 'simulation' or 'hardware'.")


def build_default_config() -> Dict[str, Any]:
    return {
        "robot": {
            "name": "Rover",
            "mode": "simulation",
            "safe_mode": True,
            "emergency_stop_enabled": True,
            "hardware": {
                "controller": "simulation",
                "servo_controller": "simulation",
                "distance_sensor": "simulation",
                "camera": "simulation",
            },
            "motion": {
                "step_height": 18.0,
                "step_length": 18.0,
                "walk_speed": 0.7,
                "turn_speed": 0.5,
                "gait_cycle_duration": 1.2,
            },
            "servo": {
                "channels": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                "min_angle": -90.0,
                "max_angle": 90.0,
                "neutral_angle": 0.0,
                "limits": {
                    "default": {"min": -90.0, "max": 90.0},
                },
            },
            "camera": {
                "source": 0,
                "width": 640,
                "height": 480,
                "fps": 30,
            },
            "safety": {
                "minimum_distance_cm": 20.0,
                "max_speed": 1.0,
                "servo_power_limit_watts": 12.0,
            },
            "web": {
                "host": "0.0.0.0",
                "port": 8000,
                "debug": False,
            },
        }
    }


def load_config(path: str | Path | None = None) -> RobotConfig:
    return RobotConfig.from_file(path)


def _default_yaml_text() -> str:
    return """robot:\n  name: Rover\n  mode: simulation\n  safe_mode: true\n  emergency_stop_enabled: true\n  hardware:\n    controller: simulation\n    servo_controller: simulation\n    distance_sensor: simulation\n    camera: simulation\n  motion:\n    step_height: 18.0\n    step_length: 18.0\n    walk_speed: 0.7\n    turn_speed: 0.5\n    gait_cycle_duration: 1.2\n  servo:\n    channels: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]\n    min_angle: -90.0\n    max_angle: 90.0\n    neutral_angle: 0.0\n  camera:\n    source: 0\n    width: 640\n    height: 480\n    fps: 30\n  safety:\n    minimum_distance_cm: 20.0\n    max_speed: 1.0\n    servo_power_limit_watts: 12.0\n  web:\n    host: 0.0.0.0\n    port: 8000\n    debug: false\n"""
