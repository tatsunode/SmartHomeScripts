import paho.mqtt.client as mqtt
import os
import json
from elasticsearch import Elasticsearch
import datetime

host = os.environ["MQTT_HOST"]
port = int(os.environ["MQTT_PORT"])

def on_connect(client, userdata, flags, response_code):
    print("status {}".format(response_code))
    client.subscribe("/gmail")


def on_message(client, userdata, msg):
    print(msg.topic, msg.payload.decode(), type(msg.payload.decode()))
    
    data = json.loads(msg.payload.decode())
    print(data)

    es = Elasticsearch(host, port=9200)
    half_day = datetime.timedelta(hours=12)
    nine_hour = datetime.timedelta(hours=9)
    receivedAt = data["receivedAt"].strip()

    receivedAtDatetime = datetime.datetime.strptime(receivedAt[:-2], "%b %d, %Y at %H:%M")

    print("AM", receivedAtDatetime)

    # received at hour format : 12:43AM ??
    if receivedAt[-2:] == "AM":
    	receivedAtDatetime = receivedAtDatetime - half_day

    # Elasticsearch accept UTC
    print("JST", receivedAtDatetime)
    receivedAtDatetime = receivedAtDatetime - nine_hour
    print("UTC", receivedAtDatetime)
 
    body = {
        "@datetime": receivedAtDatetime,
        "subject": data["subject"],
        "sender": data["fromName"],
        "address": data["fromAddress"],
    }
    es.index(index="locus-gmail", doc_type="data", body=body)


if __name__ == "__main__":

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(host, port=port, keepalive=60)

    client.loop_forever()
