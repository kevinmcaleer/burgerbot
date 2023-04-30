from burgerbot import Burgerbot
from time import time, sleep

bot = Burgerbot()

def track_object(bot, target_distance, tracking_duration):
    start_time = time()

    while time.time() - start_time < tracking_duration:
        
        if bot.distance < target_distance:
            bot.backward()
        elif bot.distance > target_distance:
            bot.forward()
        else:
            sleep(0.1)

target_distance = 50  # Set the desired distance in appropriate units (e.g., centimeters)
tracking_duration = 10  # Set the duration for tracking the object in seconds

while True:
    track_object(bot, target_distance, tracking_duration)