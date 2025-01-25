# BurgerBot
# Author: Kevin McAleer
# Date: June 2022
# Updated: 25 January 2025

# Import necessary modules
from motor import Motor, pico_motor_shim  # Motor control libraries
from pimoroni import REVERSED_DIR  # For reversing motor direction
from servo import Servo  # Servo motor control
import gc  # Garbage collection utilities
from machine import Pin  # Microcontroller pin control
from time import sleep, sleep_us, ticks_us  # Timing utilities

gc.threshold(50000)  # Configure garbage collection threshold for efficient memory management

class RangeFinder:
    """
    A class to represent an ultrasonic range finder.

    Attributes:
        trigger (Pin): The GPIO pin connected to the trigger of the sensor.
        echo (Pin): The GPIO pin connected to the echo of the sensor.
    """

    def __init__(self, trigger_pin: int = 0, echo_pin: int = 1):
        """
        Initializes the RangeFinder with specified trigger and echo pins.

        Args:
            trigger_pin (int): The pin number for the trigger signal.
            echo_pin (int): The pin number for the echo signal.
        """
        self.trigger = Pin(trigger_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)

    @property
    def distance(self) -> float:
        """
        Measures the distance to an object using the ultrasonic sensor.

        Returns:
            float: The distance to the object in centimeters.
        """
        signalon = 0
        signaloff = 0

        # Reset the trigger
        self.trigger.low()
        sleep_us(2)

        # Send a 10-microsecond pulse
        self.trigger.high()
        sleep_us(5)
        self.trigger.low()

        # Measure the echo pulse duration
        while self.echo.value() == 0:
            signaloff = ticks_us()
        while self.echo.value() == 1:
            signalon = ticks_us()

        elapsed_microseconds = signalon - signaloff
        distance_cm = (elapsed_microseconds * 0.343) / 2
        return round(distance_cm, 1)

class Burgerbot:
    """
    A class to control the BurgerBot robot.

    Attributes:
        motors (list): List of Motor objects for the robot.
        pen_servo (Servo): Servo object to control the pen.
        line_sensor (Pin): GPIO pin for the line sensor.
        range_finder (RangeFinder): Object for measuring distance using an ultrasonic sensor.
        __speed (float): Internal speed value for the motors.
    """

    MOTOR_PINS = [pico_motor_shim.MOTOR_1, pico_motor_shim.MOTOR_2]  # Motor pins
    motors = [Motor(pins) for pins in MOTOR_PINS]  # Initialize motor objects
    pen_servo = Servo(16)  # Initialize pen servo on pin 16
    line_sensor = Pin(17, Pin.IN)  # Line sensor pin
    range_finder = RangeFinder(trigger_pin=0, echo_pin=1)  # Ultrasonic range finder

    def __init__(self):
        """
        Initializes the BurgerBot with default motor configurations and speed.
        """
        # Reverse the direction of the second motor for alignment
        self.motors[1].direction(REVERSED_DIR)

        # Enable all motors and set default speed
        for motor in self.motors:
            motor.enable()
        self.speed = 0.5

    @property
    def distance(self) -> float:
        """
        Gets the distance from the range finder sensor.

        Returns:
            float: Distance to the nearest object in centimeters.
        """
        return self.range_finder.distance

    @property
    def line_detected(self) -> bool:
        """
        Checks if the line sensor detects a line.

        Returns:
            bool: True if a line is detected, False otherwise.
        """
        return self.line_sensor.value() == 1

    def pen_middle(self):
        """
        Moves the pen servo to its middle position (neutral).
        """
        self.pen_servo.to_mid()

    def pen_down(self):
        """
        Lowers the pen servo to the drawing position.
        """
        self.pen_servo.value(30)

    def pen_up(self):
        """
        Raises the pen servo to the lifted position.
        """
        self.pen_servo.value(-20)

    def forward(self, duration: float = 0.5):
        """
        Drives the robot forward for a specified duration.

        Args:
            duration (float): Time in seconds to drive forward.
        """
        for m in self.motors:
            m.speed(self.speed)
        sleep(duration)

    def backward(self, duration: float = 0.5):
        """
        Drives the robot backward for a specified duration.

        Args:
            duration (float): Time in seconds to drive backward.
        """
        for m in self.motors:
            m.speed(-self.speed)
        sleep(duration)

    def turn_left(self, duration: float = 0.5):
        """
        Turns the robot left for a specified duration.

        Args:
            duration (float): Time in seconds to turn left.
        """
        self.motors[0].speed(self.speed)
        self.motors[1].speed(-self.speed)
        sleep(duration)

    def turn_right(self, duration: float = 0.5):
        """
        Turns the robot right for a specified duration.

        Args:
            duration (float): Time in seconds to turn right.
        """
        self.motors[0].speed(-self.speed)
        self.motors[1].speed(self.speed)
        sleep(duration)

    def stop(self):
        """
        Stops the robot by disabling both motors.
        """
        for m in self.motors:
            m.disable()

    def left_motor(self, speed: float):
        """
        Sets the speed of the left motor.

        Args:
            speed (float): Speed value for the left motor (-1 to 1).
        """
        self.motors[0].speed(speed)

    def right_motor(self, speed: float):
        """
        Sets the speed of the right motor.

        Args:
            speed (float): Speed value for the right motor (-1 to 1).
        """
        self.motors[1].speed(speed)

    @property
    def speed(self) -> float:
        """
        Gets the current speed value for the motors.

        Returns:
            float: Speed value (-1 to 1).
        """
        return self.__speed

    @speed.setter
    def speed(self, value: float):
        """
        Sets the speed value for the motors, ensuring it is within the valid range.

        Args:
            value (float): Speed value (-1 to 1).

        Raises:
            ValueError: If the speed value is out of range.
        """
        if -1 <= value <= 1:
            self.__speed = value
        else:
            raise ValueError(f"Speed value should be between -1 and +1, but {value} was provided.")
