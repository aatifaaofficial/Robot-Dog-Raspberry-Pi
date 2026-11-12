from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, Iterable, Mapping


def clamp_angle(angle: float, minimum: float = -90.0, maximum: float = 90.0) -> float:
    value = float(angle)
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


def interpolate_angles(start: float, end: float, fraction: float) -> float:
    if fraction < 0.0:
        return start
    if fraction > 1.0:
        return end
    return start + (end - start) * fraction


@dataclass
class LegGeometry:
    hip_length: float = 20.0
    upper_leg_length: float = 60.0
    lower_leg_length: float = 80.0
    ground_clearance: float = 18.0

    def to_dict(self) -> Dict[str, float]:
        return {
            "hip_length": self.hip_length,
            "upper_leg_length": self.upper_leg_length,
            "lower_leg_length": self.lower_leg_length,
            "ground_clearance": self.ground_clearance,
        }


def solve_leg_ik(geometry: LegGeometry, x: float, y: float, z: float) -> Dict[str, float]:
    horizontal = math.hypot(x, y)
    if horizontal < 1e-9:
        horizontal = 1e-9
    projected = max(horizontal - geometry.hip_length, 0.0)
    distance = math.hypot(projected, z)
    if distance < 1e-9:
        return {"hip": 0.0, "hip_pitch": 0.0, "knee_pitch": 0.0}

    a = geometry.upper_leg_length
    b = geometry.lower_leg_length
    if distance > (a + b):
        distance = a + b

    cosine_rule = (a * a + b * b - distance * distance) / (2 * a * b)
    cosine_rule = max(-1.0, min(1.0, cosine_rule))
    knee = math.acos(cosine_rule)

    second_rule = (a * a + distance * distance - b * b) / (2 * a * distance)
    second_rule = max(-1.0, min(1.0, second_rule))
    hip_pitch = math.atan2(z, projected) + math.acos(second_rule)

    return {
        "hip": clamp_angle(math.degrees(math.atan2(y, x)), -90.0, 90.0),
        "hip_pitch": clamp_angle(math.degrees(hip_pitch), -90.0, 90.0),
        "knee_pitch": clamp_angle(math.degrees(math.pi - knee), -90.0, 90.0),
    }


def forward_kinematics(geometry: LegGeometry, hip: float, hip_pitch: float, knee_pitch: float) -> Dict[str, float]:
    hip_rad = math.radians(hip)
    hip_pitch_rad = math.radians(hip_pitch)
    knee_rad = math.radians(knee_pitch)

    shoulder_x = geometry.hip_length * math.cos(hip_rad)
    shoulder_y = geometry.hip_length * math.sin(hip_rad)

    x = shoulder_x + geometry.upper_leg_length * math.cos(hip_pitch_rad) + geometry.lower_leg_length * math.cos(hip_pitch_rad + knee_rad)
    y = shoulder_y + geometry.upper_leg_length * math.sin(hip_pitch_rad) + geometry.lower_leg_length * math.sin(hip_pitch_rad + knee_rad)
    z = math.sin(hip_pitch_rad) * (geometry.upper_leg_length + geometry.lower_leg_length)
    return {"x": x, "y": y, "z": z}


def stand_pose(geometry: LegGeometry | None = None) -> Dict[str, Dict[str, float]]:
    geometry = geometry or LegGeometry()
    neutral = solve_leg_ik(geometry, 0.0, 0.0, geometry.ground_clearance)
    return {
        "front_left": neutral,
        "front_right": neutral,
        "rear_left": neutral,
        "rear_right": neutral,
    }
