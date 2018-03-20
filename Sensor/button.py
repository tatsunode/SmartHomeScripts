import RPi.GPIO as GPIO
import time
ButtonPin = 17
LedPin = 18

led_status = True

def ButtonLed(ev=None):
    global led_status
    led_status = not led_status
    print("Pressed")
#    GPIO.output(LedPin, led_status)
#    if led_status:
#        print("LED OFF")
#        print()
#    else:
#        print("LED ON")
#        print()

# setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)

GPIO.setup(ButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(ButtonPin, GPIO.FALLING, callback=ButtonLed)

while True:
    time.sleep(1)
