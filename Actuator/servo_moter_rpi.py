import time
import RPi.GPIO as GPIO

pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

servo = GPIO.PWM(pin, 50)

servo.start(0.0)

for i in range(10):
