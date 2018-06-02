#!/usr/bin/python36
# -*- coding: utf-8
from time import sleep
from scapy.all import *
import paho.mqtt.client as mqtt
import os
import datetime

MQTT_HOST = os.environ["MQTT_HOST"]
MQTT_PORT = int(os.environ["MQTT_PORT"])

ADB_MAC_ADDRESSES = str(os.environ["AMAZON_DASH_BUTTON_MAC_ADDRESSES"]).strip()
ADB_MAC_LIST = ADB_MAC_ADDRESSES.split(",")

client = mqtt.Client()
client.connect(MQTT_HOST, port=MQTT_PORT, keepalive=60)



def find(pkt):
    print("find", pkt.show())
    hwsrc = str(pkt.hwsrc).strip()
    topic = "amazondashbutton/" + hwsrc
    now = str(datetime.datetime.now())
    client.publish(topic, now)
    sleep(0.5)


def start_watch():

    if ADB_MAC_LIST:
        bpf_filter = "arp && (ether src " + " || ".join(ADB_MAC_LIST) + ")"
        print(bpf_filter)
        sniff(filter=bpf_filter, prn=find)

# client.disconnect()

if __name__=="__main__":
    start_watch()
