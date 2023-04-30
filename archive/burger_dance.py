from time import sleep
from burgerbot import Burgerbot

bot = Burgerbot()
bot.speed = 0.3

while True:
    for n in range(4):
        bot.turnleft()
        sleep(1)
        bot.stop()
        sleep(1)
#         bot.forward()
#         sleep(1)
#         bot.turnleft()
#         sleep(0.3)
#     sleep(5)
