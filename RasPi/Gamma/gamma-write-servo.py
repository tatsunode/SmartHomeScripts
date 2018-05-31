import paho.mqtt.client as mqtt
import os
import time
import RPi.GPIO as GPIO


host = os.environ["MQTT_HOST"]
port = int(os.environ["MQTT_PORT"])


SERVO_PIN = 18


class Servo:

    def __init__(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SERVO_PIN, GPIO.OUT)
        self.servo = GPIO.PWM(SERVO_PIN, 50)
        self.servo.start(0.0)
        time.sleep(0.5)

    def reset_position(self):
        print("reset position")
        self.servo.ChangeDutyCycle(8.8)

    def on_position(self):
        print("on position")
        self.servo.ChangeDutyCycle(10.0)

    def off_position(self):
        print("off position")
        self.servo.ChangeDutyCycle(7.5)

    def on(self):
        self.reset_position()
        time.sleep(0.2)
        self.on_position()
        time.sleep(0.5)
        self.reset_position()
        time.sleep(0.5)

        GPIO.cleanup()

    def off(self):
        self.reset_position()
        time.sleep(0.2)
        self.off_position()
        time.sleep(0.5)
        self.reset_position()
        time.sleep(0.5)

        GPIO.cleanup()


def on_connect(client, userdata, flags, response_code):

    print("status {}".format(response_code))
    client.subscribe("light/main/#")


def on_message(client, userdata, msg):

    servo = Servo()
    value = int(msg.payload.decode())

    if value > 0:
        servo.on()
    else:
        servo.off()


if __name__=="__main__":


    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host, port=port, keepalive=60)
    client.loop_forever()
