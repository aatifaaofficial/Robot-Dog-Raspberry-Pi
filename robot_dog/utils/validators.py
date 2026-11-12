from __future__ import annotations

from typing import Iterable, Sequence


def validate_channel(channel: int, valid_channels: Iterable[int] | None = None) -> int:
    value = int(channel)
    channels = list(valid_channels) if valid_channels is not None else list(range(16))
    if value not in channels:
        raise ValueError(f"Invalid servo channel {channel!r}. Allowed channels: {channels}")
    return value


def clamp_angle(angle: float, minimum: float = -90.0, maximum: float = 90.0) -> float:
    value = float(angle)
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


def validate_gpio_pin(pin: int) -> int:
    pin = int(pin)
    if pin < 0 or pin > 40:
        raise ValueError("GPIO pin out of range for Raspberry Pi (0-40).")
    return pin


def validate_distance(distance_cm: float) -> float:
    distance = float(distance_cm)
    if distance < 0:
        raise ValueError("Distance cannot be negative.")
    return distance
