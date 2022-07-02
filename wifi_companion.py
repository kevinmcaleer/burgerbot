# Pico Wifi Module
# Pico Companion code

from machine import Pin, UART
uart = UART(id=0, rx=Pin(1), tx=Pin(0), baudrate=9600)

print("hello World")
uart.write("hello")
while True:
    if uart.any() > 0:
        try:
            msg = str(uart.read(),'utf-8','ignore')
            print(msg)
        except:
            pass
        