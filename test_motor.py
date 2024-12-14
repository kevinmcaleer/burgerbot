from motor import Motor
from time import sleep

motor_1 = Motor(1,2)
motor_2 = Motor(3,4)
motor_1.speed = 0.5
motor_2.speed = 0.5

motor_1.stop()
motor_2.stop()


def do_test():
    motor_1.backward()
    sleep(1)
    motor_1.stop()
    sleep(1)

    motor_1.forward()
    sleep(1)
    motor_1.stop()
    sleep(1)

    motor_2.backward()
    sleep(1)

    motor_1.stop()
    sleep(1)

    motor_2.forward()
    sleep(1)

    motor_2.stop()
    sleep(1)
    

