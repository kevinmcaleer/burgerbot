from time import sleep
from range_finder import RangeFinder

distance = RangeFinder(trigger_pin=6, echo_pin=5)

while True:
    
    print(f" Distance = {distance.distance}")
    
    sleep(1)