from robot_dog.motion.kinematics import LegGeometry, clamp_angle, interpolate_angles, solve_leg_ik


def test_clamp_angle():
    assert clamp_angle(200, -90, 90) == 90
    assert clamp_angle(-200, -90, 90) == -90


def test_interpolate_angles():
    assert interpolate_angles(0, 10, 0.5) == 5


def test_solve_leg_ik_returns_angles():
    geometry = LegGeometry(hip_length=20.0, upper_leg_length=60.0, lower_leg_length=80.0)
    result = solve_leg_ik(geometry, 0.0, 0.0, 50.0)
    assert set(result) == {"hip", "hip_pitch", "knee_pitch"}
