from gtts import gTTS
import paho.mqtt.client as mqtt
import pychromecast
import os

host = os.environ["MQTT_HOST"]
port = os.environ["MQTT_PORT"]

def on_connect(client, userdata, flags, response_code):
    client.subscribe("google-home-notification")

def on_message(client, userdata, msg):
    speak(str(msg.payload))

def speak(text):

    tts = gTTS(text=text, lang="ja")
    filename = "notification.mp3"
    # MP3_FILE_DIR = "/var/www/html/mp3"
    MP3_FILE_DIR = "./"

    tts.save(os.path.join(MP3_FILE_DIR, filename))

    server_ip_address = host
    device_ip_address = "192.168.10.4"

    url = "http://" + server_ip_address + "/mp3/" + filename

    cast= pychromecast.Chromecast(device_ip_address)
    cast.wait()

    mc = cast.media_controller
    mc.play_media(url, "audio/mp3")
