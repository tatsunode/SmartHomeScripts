import time
import paho.mqtt.client as mqtt
import os
import requests

host = os.environ["MQTT_HOST"]
port = int(os.environ["MQTT_PORT"])
nature_remo_key = os.environ["NATURE_REMO_KEY"]

client = mqtt.Client()

client.connect(host, port=port, keepalive=60)

endpoint = "https://api.nature.global/1/devices"
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + nature_remo_key
}

response = requests.get(endpoint, headers=headers).json()

if response:
    device_data = response[0]
    humidity = device_data["newest_events"]["hu"]["val"]
    temperature = device_data["newest_events"]["te"]["val"]
    illuminance = device_data["newest_events"]["il"]["val"]

    print(humidity, temperature, illuminance)

    client.publish("humidity/main", humidity)
    time.sleep(1) 
    client.publish("temperature/main", temperature)
    time.sleep(1) 
    client.publish("illuminance/main", temperature)
    time.sleep(1) 
