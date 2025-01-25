from machine import Pin
from time import ticks_us, sleep_us

class RangeFinder():
    
    def __init__(self,trigger_pin:int = 0, echo_pin:int = 1):
        self.trigger = Pin(trigger_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)
    
    @property
    def distance(self):
        """ Returns the distance in cm """
        
        # set the signal on & off times to zero
        signalon = 0
        signaloff = 0
        
        # reset the trigger
        self.trigger.low()
        sleep_us(2)
        
        self.trigger.high()
        sleep_us(5)
        self.trigger.low()
        
        while self.echo.value() == 0:
            signaloff = ticks_us()
        while self.echo.value() == 1:
            signalon = ticks_us()
            
        elapsed_microseconds = signalon - signaloff
        self.duration = elapsed_microseconds
        self.distance_to_object = (elapsed_microseconds * 0.343) / 2
        return round(self.distance_to_object / 10 ,1)
    