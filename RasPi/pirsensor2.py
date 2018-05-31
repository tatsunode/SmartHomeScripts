import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin1 = 4
pin2 = 25


def main():

    GPIO.setup(pin1, GPIO.IN)
    GPIO.setup(pin2, GPIO.IN)

    while True:

        pin1out = GPIO.input(pin1)
        pin2out = GPIO.input(pin2)

        print(pin1out, pin2out)
        time.sleep(1)

    GPIO.cleanup()


if __name__=="__main__":
    main()
