from machine import Pin, PWM

class Motor:
    def __init__(self, motor_pin_a, motor_pin_b, pwm_freq=1000):
        # Initialize motor pins with PWM
        self.pwm_a = PWM(Pin(motor_pin_a))
        self.pwm_b = PWM(Pin(motor_pin_b))
        self.pwm_a.freq(pwm_freq)
        self.pwm_b.freq(pwm_freq)
        self._speed = 0  # Speed range: 0 (stop) to 1 (full speed)

    def forward(self):
        # Set motor to move forward
        self.pwm_b.duty_u16(int(self._speed * 65535))
        self.pwm_a.duty_u16(0)  # Reverse pin stopped

    def backward(self):
        # Set motor to move backward
        self.pwm_b.duty_u16(0)  # Forward pin stopped
        self.pwm_a.duty_u16(int(self._speed * 65535))

    def stop(self):
        # Stop the motor
        self.pwm_a.duty_u16(0)
        self.pwm_b.duty_u16(0)

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if 0 <= value <= 1:
            self._speed = value
        else:
            raise ValueError("Speed must be between 0 and 1")
