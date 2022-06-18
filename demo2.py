from time import sleep
from burgerbot import Burgerbot
from time import sleep

mac = Burgerbot()
mac.speed = 0.3
# mac.forward()
mac.turnleft()
sleep(1)
mac.stop()

# mac.backward()
mac.turnright()
sleep(1)
mac.stop()