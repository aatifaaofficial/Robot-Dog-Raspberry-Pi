from robot_dog.motion.gait import GaitParameters, generate_walk_cycle


def test_generate_walk_cycle():
    cycle = generate_walk_cycle(18.0, 20.0, 1.2)
    assert len(cycle) == 4
    assert all("phase" in item for item in cycle)


def test_gait_parameters_as_dict():
    params = GaitParameters(step_height=15.0, step_length=30.0)
    data = params.as_dict()
    assert data["step_height"] == 15.0
