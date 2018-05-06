import paho.mqtt.client as mqtt
import os

host = os.environ["MQTT_HOST"]
port = int(os.environ["MQTT_PORT"])

print(host, port)

topic = "test/#"

def on_connect(client, userdata, flags, response_code):
    print("status {}".format(response_code))

    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(msg.topic, str(msg.payload))

if __name__ == "__main__":

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(host, port=port, keepalive=60)

    client.loop_forever()
