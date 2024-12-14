# button test

from machine import Pin
from pimoroni import Button
from time import sleep


button_1 = Button(0)


print('setting up buttons')
while True:
    print(button_1.is_pressed)
  
    if button_1.is_pressed:
        print('button 1 press')

    sleep(0.5)
    