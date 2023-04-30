# Line following

from machine import Pin
from time import sleep

line_sensor: Pin = Pin(17, Pin.IN)

while True:
    print(f'line: {line_sensor.value()}')
    sleep(1)