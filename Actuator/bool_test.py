import RPi.GPIO as GPIO
import time

LedPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LedPin, GPIO.OUT)
GPIO.output(LedPin, GPIO.HIGH)

time.sleep(1)
GPIO.cleanup()
