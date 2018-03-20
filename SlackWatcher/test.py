from slackclient import SlackClient
import time

sc = SlackClient(slack_token)

if sc.rtm_connect({"channel":"#light_switch"}):
    while True:
        print(sc.rtm_read())
        time.sleep(1)

else:
    print("Connection Failed")
