from time import sleep
import paho.mqtt.client as mqtt
import os

host = os.environ["MQTT_HOST"]
port = int(os.environ["MQTT_PORT"])

print(host, port)

client = mqtt.Client()

client.connect(host, port=port, keepalive=60)

topic = "test/alpha"

for i in range(10):
    client.publish(topic, "value" + str(i))
    sleep(3)

client.disconnect()
