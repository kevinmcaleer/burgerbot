from demo1 import SPEED_EXTENT


# BurgerBot
# Kevin McAleer
# June 2022

from motor import Motor, pico_motor_shim

class Burgerbot:

    # Create a list of motors
    MOTOR_PINS = [pico_motor_shim.MOTOR_1, pico_motor_shim.MOTOR_2]
    motors = [Motor(pins) for pins in MOTOR_PINS]
    __speed = 0

    def __init__(self):

        # Use the settings below to configure the motors so they turn in the same direction
        
        motors[0].direction(REVERSED_DIR)
        # motors[1].direction(REVERSED_DIR)

    def forward(self):
        self.motors[0].speed = self.speed
        pass
    
    def backward(self):
        pass

    def turnleft(self):
        pass
    
    def turnright(self):
        pass

    def stop(self):
        # Disable the motors
        for m in self.motors:
            m.disable()

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if 0 < speed < 100:
            self.__speed = value
        else:
            print(f"Speed value should be between 0 and 100, however {value} was provided")

