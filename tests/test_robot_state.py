from robot_dog.control.robot_state import RobotState


def test_robot_state_snapshot():
    state = RobotState(mode="simulation", status="active", walking=True)
    snapshot = state.snapshot()
    assert snapshot["mode"] == "simulation"
    assert snapshot["walking"] is True


def test_robot_state_update():
    state = RobotState()
    state.update(status="ready", battery_level=75)
    assert state.status == "ready"
    assert state.battery_level == 75
