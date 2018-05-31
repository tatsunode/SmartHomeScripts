import RPi.GPIO as GPIO
import time

pin = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)

while True:

    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.1)

GPIO.cleanup()
