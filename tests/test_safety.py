from robot_dog.utils.validators import clamp_angle, validate_distance


def test_clamp_angle_safety_bound():
    assert clamp_angle(40, -30, 30) == 30


def test_validate_distance():
    assert validate_distance(15.0) == 15.0
