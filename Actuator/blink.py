import RPi.GPIO as GPIO
import time

pins = [5,6,13,16,19,20]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)

while True:

    for pin in pins:
    	GPIO.output(pin, GPIO.HIGH)
    	time.sleep(0.2)
    	GPIO.output(pin, GPIO.LOW)
    	time.sleep(0.2)

GPIO.cleanup()
