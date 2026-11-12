# Robot Dog-Raspberry Pi

A modular quadruped robot dog project built in Python for Raspberry Pi and simulation environments.

## Overview

This repository contains a production-style skeleton for a four-legged robot dog. The project is designed to support:

- Simple simulation mode for development on desktop systems
- Raspberry Pi compatible hardware mode when required libraries are present
- Servo motion control with angle validation and calibration hooks
- Gait generation and walking commands
- Object, person, and obstacle detection abstractions
- Voice command parsing
- Web status dashboard

## Quick start

1. Create a virtual environment and activate it.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run the simulator:
   `python -m robot_dog.main`
4. Or execute the simulator script:
   `python scripts/run_simulation.py`

## Default behavior

The project defaults to simulation mode so it runs on a normal development machine without hardware.

To switch to hardware mode, edit `config/robot.yaml` and set:

```yaml
robot:
  mode: hardware
```

## Project structure

- `config/` — robot, camera, servo, and safety configuration files
- `robot_dog/` — main application package
- `scripts/` — environment checks and hardware utilities
- `tests/` — unit tests for config, gait, motion, and command parsing
- `docs/` — installation, calibration, safety, and troubleshooting docs

## Safety

The project includes explicit safety guidelines for hardware use, including servo power isolation and Raspberry Pi GPIO voltage constraints.

## Notes

This repository intentionally supports simulation as the default path to keep the project usable in a developer workstation environment while still providing a path to real hardware.

