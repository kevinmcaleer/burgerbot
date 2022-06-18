from time import sleep
from burgerbot import Burgerbot
from time import sleep

mac = Burgerbot()
mac.speed = 1
mac.forward()
sleep(1)
mac.stop()