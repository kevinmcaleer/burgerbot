from time import sleep
from burgerbot import Burgerbot

mac = Burgerbot()
mac.speed = 50
# mac.forward()
# mac.turnleft()
# sleep(1)
# mac.stop()
# 
# # mac.backward()
# mac.turnright()
# sleep(1)
# mac.stop()

# mac.backward()
mac.forward()
sleep(2)
mac.stop()
