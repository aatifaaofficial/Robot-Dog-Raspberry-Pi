from __future__ import annotations

from robot_dog.config import load_config


def main() -> None:
    config = load_config()
    print(f"Mode: {config.mode}")
    print(f"Name: {config.robot_name}")


if __name__ == "__main__":
    main()
