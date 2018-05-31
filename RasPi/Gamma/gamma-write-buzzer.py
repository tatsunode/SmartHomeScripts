import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
import os

host = os.environ["MQTT_HOST"]
port = int(os.environ["MQTT_PORT"])

print(host, port)

pin = 16
topic = "buzzer/main"


def on_connect(client, userdata, flags, response_code):
    print("status {}".format(response_code))

    client.subscribe(topic)

def on_message(client, userdata, msg):

    value = int(msg.payload.decode())
    print(msg.topic, value)

    GPIO.cleanup()

    if value > 0:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)

        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.3)


    else:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)

        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.3)



if __name__ == "__main__":

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host, port=port, keepalive=60)
    client.loop_forever()

