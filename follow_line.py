from burgerbot import Burgerbot

bot = Burgerbot()
bot.speed = 0.25

while True:
    if bot.line_detected:
        bot.forward(duration = 0.001)
    else:
        bot.turnleft(duration = 0.001)
        bot.forward(duration = 0.001)
