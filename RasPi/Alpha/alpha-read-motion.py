import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
import os

host = os.environ["MQTT_HOST"]
port = int(os.environ["MQTT_PORT"])

motion_pin1 = 4
motion_pin2 = 25

def main():

    client = mqtt.Client()
    client.connect(host, port=port, keepalive=60)

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(motion_pin1, GPIO.IN)
    GPIO.setup(motion_pin2, GPIO.IN)

    while True:

        pin1_value = 0
        pin2_value = 0

        for i in range(10):
    
            pin1_value += GPIO.input(motion_pin1)
            pin2_value += GPIO.input(motion_pin2)
            time.sleep(1.0)

        client.publish("motion/main/1", pin1_value)
        client.publish("motion/main/2", pin2_value)

        print(pin1_value, pin2_value)

    client.disconnect()
    GPIO.cleanup()

if __name__=="__main__":
    main()




