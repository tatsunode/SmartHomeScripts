import paho.mqtt.client as mqtt
import os
from elasticsearch import Elasticsearch
import datetime

host = os.environ["MQTT_HOST"]
port = int(os.environ["MQTT_PORT"])

def on_connect(client, userdata, flags, response_code):
    print("status {}".format(response_code))
    client.subscribe("+/main")


def on_message(client, userdata, msg):
    print(msg.topic, msg.payload.decode())
    
    es = Elasticsearch(host, port=9200)

    # Elasticsearch accept UTC
    nine_hour = datetime.timedelta(hours=9)
    timestamp = datetime.datetime.now() - nine_hour

    if msg.topic == "temperature/main":
        body = {
            "@datetime": timestamp,
            "device": "NatureRemo",
            "temperature": float(msg.payload.decode())
        }
        es.index(index="locus-sensor-temperature", doc_type="data", body=body)
         
    elif msg.topic == "humidity/main":
        body = {
            "@datetime": timestamp,
            "device": "NatureRemo",
            "humidity": float(msg.payload.decode())
        }
        es.index(index="locus-sensor-humidity", doc_type="data", body=body)
 
    elif msg.topic == "illuminance/main":
        body = {
            "@datetime": timestamp,
            "device": "NatureRemo",
            "illuminance": float(msg.payload.decode())
        }
        es.index(index="locus-sensor-illuminance", doc_type="data", body=body)


if __name__ == "__main__":

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(host, port=port, keepalive=60)

    client.loop_forever()
