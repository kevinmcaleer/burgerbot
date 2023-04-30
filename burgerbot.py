# BurgerBot
# Kevin McAleer
# June 2022

from motor import Motor, pico_motor_shim
from pimoroni import REVERSED_DIR
from servo import Servo
import gc
from machine import Pin
from time import sleep, sleep_us, ticks_us

gc.threshold(50000) # setup garbage collection

class RangeFinder():
    
    def __init__(self,trigger_pin:int = 0, echo_pin:int = 1):
        self.trigger = Pin(trigger_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)
    
    @property
    def distance(self):
        """ Returns the distance in cm """
        
        # set the signal on & off times to zero
        signalon = 0
        signaloff = 0
        
        # reset the trigger
        self.trigger.low()
        sleep_us(2)
        
        self.trigger.high()
        sleep_us(5)
        self.trigger.low()
        
        while self.echo.value() == 0:
            signaloff = ticks_us()
        while self.echo.value() == 1:
            signalon = ticks_us()
            
        elapsed_microseconds = signalon - signaloff
        self.duration = elapsed_microseconds
        self.distance_to_object = (elapsed_microseconds * 0.343) / 2
        return round(self.distance_to_object / 10 ,1) 

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
    echo_pin = 0
    trigger_pin = 1
    line_sensor = Pin(17, Pin.IN)
    range_finder = RangeFinder(echo_pin=echo_pin, trigger_pin=trigger_pin)
    
    def __init__(self):
        """ Initialize the Burgerbot """
        # Use the settings below to configure the motors so they turn in the same direction
        
        # self.motors[0].direction(REVERSED_DIR)
        self.motors[1].direction(REVERSED_DIR)
        # self.pen_servo.enable()
        # self.pen_servo.to_mid()
        for motor in self.motors:
            motor.enable()
        self.speed = 0.5

    @property
    def distance(self):
        return self.range_finder.distance

    @property
    def line_detected(self)->bool:
        if self.line_sensor.value() == 1:
            return True
        else:
            return False

    def pen_middle(self):
        self.pen_servo.to_mid()

    def pen_down(self):
        self.pen_servo.value(30)

    def pen_up(self):
        self.pen_servo.value(-20)

    def forward(self, duration=0.5):        
        """ Drive the motors forward """
        for m in self.motors:
            m.speed(self.speed)
        sleep(duration)
    
    def backward(self, duration=0.5):
        """ Drive the motors backward """
        for m in self.motors:
            m.speed(-self.speed)
        sleep(duration)
        
    def turnleft(self, duration=0.5):
        """ Turn the motors left """

        # set the speed of the motors
        self.motors[0].speed(self.speed)
        self.motors[1].speed(-self.speed) 
        sleep(duration)       
    
    def turnright(self, duration=0.5):
        """ Turn the motors right """

        # set the speed of the motors
        self.motors[0].speed(-self.speed)
        self.motors[1].speed(self.speed)  
        sleep(duration)

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