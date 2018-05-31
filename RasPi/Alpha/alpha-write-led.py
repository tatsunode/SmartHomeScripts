import paho.mqtt.client as mqtt
import os
import RPi.GPIO as GPIO

host = os.environ["MQTT_HOST"]
port = int(os.environ["MQTT_PORT"])

LED_PINS = {
    "green": 17,
    "yellow": 18,
    "red": 23
}

GPIO.setmode(GPIO.BCM)

for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

print(host, port)


def on_led_connect(client, userdata, flags, response_code):
    print("status {}".format(response_code))
    client.subscribe("led/main/#")


def on_led_message(client, userdata, msg):

    topics = msg.topic.split("/")

    if len(topics) >= 3:
        color = topics[2]
        value = True if int(msg.payload.decode()) > 0 else False
        print(color, value)
        led(color, on=value)


def led(color, on=False, light_type="on"):

    pin = LED_PINS.get(color)
    value = GPIO.HIGH if on else GPIO.LOW
    GPIO.output(pin, value) 


if __name__ == "__main__":

    led_client = mqtt.Client()
    led_client.on_connect = on_led_connect
    led_client.on_message = on_led_message
    led_client.connect(host, port=port, keepalive=60)
    led_client.loop_forever()
