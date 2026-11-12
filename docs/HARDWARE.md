# Hardware Guide

This project supports simulation by default. Hardware mode is only used when the robot configuration switches to `hardware` and the required libraries are present.

## Recommended components

- Raspberry Pi 4 or 5
- 12 servo motors
- PCA9685 controller
- Raspberry Pi camera or USB camera
- HC-SR04 ultrasonic sensor
- Dedicated servo power supply

## Important safety rules

- Never connect servo power directly to Raspberry Pi GPIO.
- Use a separate regulated power source for the servo rail.
- Use a proper level shifter for 5V echo signals.
