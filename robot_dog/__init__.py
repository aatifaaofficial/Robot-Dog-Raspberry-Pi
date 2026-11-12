"""Robot dog package."""

from .application import RobotDogApplication
from .config import RobotConfig, load_config

__version__ = "0.1.0"
__all__ = ["RobotDogApplication", "RobotConfig", "load_config"]
