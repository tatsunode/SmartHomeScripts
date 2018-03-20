import wiringpi
import time
import sys

servo_pin = 18
set_degree = 24

print(set_degree)

wiringpi.wiringPiSetupGpio()

print("wiringPi setup")

wiringpi.pinMode(servo_pin, wiringpi.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.PWM_OUTPUT)
wiringpi.pwmSetClock(400)
wiringpi.pwmSetRange(1024)

print("wiringpi setup")

if -90 <= set_degree <= 90:
    move_deg = int(81 + 41 / 90 * 45)
    print("calculated move deg", move_deg)
    wiringpi.pwmWrite(servo_pin, move_deg)
