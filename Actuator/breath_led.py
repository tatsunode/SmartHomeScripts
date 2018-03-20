import RPi.GPIO as GPIO
import time

pin = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

p = GPIO.PWM(pin, 100)
p.start(0)

while True:
    for dc in range(0,101,4):
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)

    for dc in range(100,-1,-4):
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)
