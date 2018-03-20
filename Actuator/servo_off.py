import time
import RPi.GPIO as GPIO

def setup():
    pin = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    servo = GPIO.PWM(pin, 50)
    servo.start(0.0)
    time.sleep(0.5)
    return servo

def reset_position(servo):
    print("reset")
    servo.ChangeDutyCycle(8.8)
    time.sleep(0.5)

def on(servo):
    print("on")
    servo.ChangeDutyCycle(10.0)
    time.sleep(0.5)

def off(servo):
    print("off")
    servo.ChangeDutyCycle(7.5)
    time.sleep(0.5)


if __name__=="__main__":

    servo = setup()

    reset_position(servo)
    time.sleep(0.1)

    off(servo)
    time.sleep(0.1)

    reset_position(servo)
    time.sleep(0.1)

    GPIO.cleanup()
