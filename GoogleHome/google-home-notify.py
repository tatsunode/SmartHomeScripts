from gtts import gTTS
import paho.mqtt.client as mqtt
import pychromecast
import os
from datetime import datetime as dt
import time
import shutil

DEFAULT_VOLUME = 0.1

host = os.environ["MQTT_HOST"]
port = int(os.environ["MQTT_PORT"])

def on_connect(client, userdata, flags, response_code):
    client.subscribe("google-home/#")

def on_message(client, userdata, msg):

    if msg.topic == "google-home/notification":
    	speak(str(msg.payload.decode()))

    elif msg.topic == "google-home/alert":
    	speak(str(msg.payload.decode()), volume=0.3)


def speak(text, volume=0.1):

    try:
        tts = gTTS(text=text, lang="ja")

        MP3_FILE_DIR = "/var/www/html/mp3"
        filename = str(dt.now().minute) + str(dt.now().second) + "-notification.mp3"
        filepath = os.path.join(MP3_FILE_DIR, filename)

        tts.save(filepath)

    except AssertionError:
        # No text to send TTS
        return

    server_ip_address = host
    device_ip_address = "192.168.10.4"

    url = "http://" + server_ip_address + "/mp3/" + filename

    cast= pychromecast.Chromecast(device_ip_address)
    cast.set_volume(volume)
    cast.wait()

    mc = cast.media_controller
    mc.play_media(url, "audio/mp3")

    while not mc.is_idle:
        time.sleep(1)

    cast.set_volume(DEFAULT_VOLUME)
    cast.quit_app()


if __name__=="__main__":

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(host, port=port, keepalive=60)
    client.loop_forever()
