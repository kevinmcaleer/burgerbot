# BurgerBot
# Kevin McAleer
# June 2022

from motor import Motor, pico_motor_shim
from pimoroni import REVERSED_DIR
from servo import Servo
from phew import connect_to_wifi, logging, access_point, dns, server
from phew.template import render_template
from phew.server import redirect
import gc
gc.threshold(50000) # setup garbage collection

# MOTOR_1 = machine.Pin(6, machine.PIN_OUT)
# MOTOR_1_SPEED = machine.Pin(7, ,machine.PIN_OUT)
# MOTOR_2 = machine.Pin(27, machine.PIN_OUT)
# MOTOR_2_SPEED = machine.Pin(26, ,machine.PIN_OUT)


# @server.route("/penup", methods=["POST"])
# def penup():
#     global command
#     command = "penup"
#     return render_template("index.html", command=command)

class Burgerbot:

    # Create a list of motors
    MOTOR_PINS = [pico_motor_shim.MOTOR_1, pico_motor_shim.MOTOR_2]
    motors = [Motor(pins) for pins in MOTOR_PINS]
    __speed = 0
    pen_servo = Servo(16)
    

    
    def __init__(self):
        """ Initialize the Burgerbot """
        # Use the settings below to configure the motors so they turn in the same direction
        
        # self.motors[0].direction(REVERSED_DIR)
        self.motors[1].direction(REVERSED_DIR)
        # self.pen_servo.enable()
        # self.pen_servo.to_mid()

    def pen_middle(self):
        self.pen_servo.to_mid()

    def pen_down(self):
        self.pen_servo.value(30)

    def pen_up(self):
        self.pen_servo.value(-20)

    def forward(self):        
        """ Drive the motors forward """
        for m in self.motors:
            m.enable()
            m.speed(self.speed)
    
    def backward(self):
        """ Drive the motors backward """
        for m in self.motors:
            m.enable()
            m.speed(-self.speed)
        
    def turnleft(self):
        """ Turn the motors left """

        # enable the motors
        self.motors[0].enable()
        self.motors[1].enable()

        # set the speed of the motors
        self.motors[0].speed(self.speed)
        self.motors[1].speed(-self.speed)        
    
    def turnright(self):
        """ Turn the motors right """

        # enable the motors
        self.motors[0].enable()
        self.motors[1].enable()

        # set the speed of the motors
        self.motors[0].speed(-self.speed)
        self.motors[1].speed(self.speed)  

    def stop(self):
        """ Stop the motors """

        # Disable the motors
        for m in self.motors:
            m.disable()
            
    def left_motor(self, speed):
        self.motors[0].speed(speed)
        
    def right_motor(self, speed):
        self.motors[1].speed(speed)

    @property
    def speed(self):
        """ Get the speed of the motors """

        return self.__speed

    @speed.setter
    def speed(self, value):
        """ Set the speed of the motors """

        # Checl the speed value is within the range we expect (-1 to 1)
        if -1 <= value <= 1:
            self.__speed = value
#             for m in self.motors:
#                 m.speed(self.__speed)
        else:
            print(f"Speed value should be between -1 and +1, however {value} was provided")