from robot_dog.config import RobotConfig, load_config


def test_default_config_loads():
    config = load_config()
    assert config.mode == "simulation"
    assert config.robot_name == "Rover"


def test_robot_config_validation():
    config = RobotConfig(mode="hardware")
    config.validate()
    assert config.mode == "hardware"
