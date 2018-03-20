from slackclient import SlackClient
import time, os, subprocess

TARGET_CHANNEL_ID = "C7TK54PEV"


def run(message):
    if message == "ON":
        subprocess.call(["/usr/bin/python", "servo_on.py"])
    elif message == "OFF":
        subprocess.call(["/usr/bin/python", "servo_off.py"])


def watch():
    
    slack_token = os.environ["SLACK_API_TOKEN"]
    sc = SlackClient(slack_token)

    read_latest = False

    if sc.rtm_connect():
        print "Connected"
        while True:
            events = sc.rtm_read()
            for event in events:
                print event

                if event['type'] != 'message':
                    continue
                if event['channel'] != TARGET_CHANNEL_ID:
                    continue
                if not read_latest:
                    read_latest = True
                    continue
                if 'username' not in event or event['username'] != 'IFTTT':
                    continue
                attachment = event['attachments'][0]
                text = attachment['text']

                if 'on' in text:
                    print "ON"
                    run(message="ON")
                elif 'off' in text:
                    print "OFF"
                    run(message="OFF")

            time.sleep(0.2)
    else:
        print "Connection Failed"


if __name__=="__main__":
    watch()
