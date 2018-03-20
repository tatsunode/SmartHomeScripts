import RPi.GPIO as GPIO
import time

pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)

while True:

    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.3)

GPIO.cleanup()
