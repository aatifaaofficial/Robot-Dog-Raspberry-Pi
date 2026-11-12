import logging
from typing import Optional


def configure_logging(log_level: str = "INFO") -> logging.Logger:
    level = getattr(logging, str(log_level).upper(), logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        force=True,
    )
    return logging.getLogger("robot_dog")
