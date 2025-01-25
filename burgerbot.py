# BurgerBot
# Author: Kevin McAleer
# Date: June 2022
# Updated: 25 January 2025

# Import necessary modules
from motor import Motor, pico_motor_shim  # Motor control libraries
from pimoroni import REVERSED_DIR  # For reversing motor direction
from servo import Servo  # Servo motor control
from phew import connect_to_wifi, logging, access_point, dns, server  # Networking utilities
from phew.template import render_template  # HTML template rendering
from phew.server import redirect  # HTTP redirection
import gc  # Garbage collection utilities
from machine import Pin  # Microcontroller pin control

gc.threshold(50000)  # Configure garbage collection threshold for efficient memory management

class Burgerbot:
    """
    A class representing the BurgerBot robot.
    Includes functionality for motor control, line detection, and servo control.
    """

    # Define motor pins and initialize motor objects
    MOTOR_PINS = [pico_motor_shim.MOTOR_1, pico_motor_shim.MOTOR_2]  # Pins for the motors
    motors = [Motor(pins) for pins in MOTOR_PINS]  # Create motor instances

    __speed = 0  # Default motor speed
    pen_servo = Servo(16)  # Initialize pen servo on pin 16
    line_sensor = Pin(17, Pin.IN)  # Initialize line sensor on pin 17 (input mode)

    def __init__(self):
        """
        Initialize the BurgerBot by configuring motor directions.
        """
        # Reverse the direction of the second motor to ensure consistent movement
        self.motors[1].direction(REVERSED_DIR)

    @property
    def line_detected(self) -> bool:
        """
        Check if the line sensor detects a line.
        
        Returns:
            bool: True if a line is detected, False otherwise.
        """
        return self.line_sensor.value() == 1

    # Servo control methods
    def pen_middle(self):
        """
        Move the pen servo to its middle position.
        """
        self.pen_servo.to_mid()

    def pen_down(self):
        """
        Move the pen servo to the down position (e.g., for drawing).
        """
        self.pen_servo.value(30)

    def pen_up(self):
        """
        Move the pen servo to the up position (e.g., for lifting the pen).
        """
        self.pen_servo.value(-20)

    # Motor movement methods
    def forward(self):
        """
        Drive both motors forward at the configured speed.
        """
        for m in self.motors:
            m.enable()
            m.speed(self.speed)

    def backward(self):
        """
        Drive both motors backward at the configured speed.
        """
        for m in self.motors:
            m.enable()
            m.speed(-self.speed)

    def turn_left(self):
        """
        Turn the robot left by driving the motors in opposite directions.
        """
        self.motors[0].enable()
        self.motors[1].enable()
        self.motors[0].speed(self.speed)
        self.motors[1].speed(-self.speed)

    def turn_right(self):
        """
        Turn the robot right by driving the motors in opposite directions.
        """
        self.motors[0].enable()
        self.motors[1].enable()
        self.motors[0].speed(-self.speed)
        self.motors[1].speed(self.speed)

    def stop(self):
        """
        Stop both motors by disabling them.
        """
        for m in self.motors:
            m.disable()

    # Individual motor control methods
    def left_motor(self, speed):
        """
        Set the speed of the left motor.

        Args:
            speed (float): Speed of the left motor (-1 to 1).
        """
        self.motors[0].speed(speed)

    def right_motor(self, speed):
        """
        Set the speed of the right motor.

        Args:
            speed (float): Speed of the right motor (-1 to 1).
        """
        self.motors[1].speed(speed)

    # Speed property methods
    @property
    def speed(self) -> float:
        """
        Get the current speed of the motors.

        Returns:
            float: Speed of the motors (-1 to 1).
        """
        return self.__speed

    @speed.setter
    def speed(self, value: float):
        """
        Set the speed of the motors, ensuring the value is within the valid range.

        Args:
            value (float): Desired motor speed (-1 to 1).

        Raises:
            ValueError: If the speed value is out of range.
        """
        if -1 <= value <= 1:
            self.__speed = value
        else:
            raise ValueError(f"Speed value should be between -1 and +1, but {value} was provided.")
