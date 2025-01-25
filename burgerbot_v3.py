from motor import Motor
from range_finder import RangeFinder
from machine import Pin

class BurgerBot():
    left_motor = Motor(1,2)
    right_motor = Motor(3,4)
    range_finder = RangeFinder(6,5)
    led = Pin("LED", Pin.OUT)
    led.value(1)

    def __init__(self):
        self.left_motor.speed = 0.5
        self.right_motor.speed = 0.5

    def forward(self):
        self.left_motor.forward()
        self.right_motor.forward()

    def backward(self):
        self.left_motor.backward()
        self.right_motor.backward()

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()

    def turn_left(self): 
        self.left_motor.backward()
        self.right_motor.forward()

    def turn_right(self):
        self.left_motor.forward()
        self.right_motor.backward()

    def follow(self):
        distance = self.range_finder.distance
        if distance < 10:
            self.stop()
        else:
            self.forward()
        if distance < 5:
            self.backward()

    def avoid(self):
        distance = self.range_finder.distance
        if distance < 10:
            self.turn_left()
        else:
            self.forward()

        