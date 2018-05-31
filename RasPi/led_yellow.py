import RPi.GPIO as GPIO
import time

green_pin = 17
yellow_pin = 18
red_pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(yellow_pin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(red_pin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(green_pin, GPIO.OUT, initial=GPIO.HIGH)

while True:

    GPIO.output(green_pin, GPIO.LOW)
    GPIO.output(yellow_pin, GPIO.LOW)
    GPIO.output(red_pin, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(green_pin, GPIO.HIGH)
    GPIO.output(yellow_pin, GPIO.HIGH)
    GPIO.output(red_pin, GPIO.HIGH)
    time.sleep(0.1)

GPIO.cleanup()
