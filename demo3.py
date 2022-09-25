from time import sleep
from burgerbot import Burgerbot

mac = Burgerbot()

delay = 1.0
while True:
    mac.pen_middle()
    print('middle')
    sleep(delay)
    mac.pen_down()
    print('down')
    sleep(delay)
    mac.pen_up()
    print('up')
    sleep(delay)
