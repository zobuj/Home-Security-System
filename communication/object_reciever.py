
# will be running in the background awaiting to see if a person will be seen, sends a message to me if a person is seen

import communication.config as config
 
from twilio.rest import Client
import paho.mqtt.client as mqtt

person_detected = False
count=0

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("CoreElectronics/test")
    client.subscribe("CoreElectronics/topic")
 

def on_message(client, userdata, msg):
    account_sid = config.ACCOUNT_SID
    auth_token = config.AUTH_TOKEN
    clientPhone = Client(account_sid, auth_token)


    global person_detected
    global count
    if person_detected == False and count > 0:

        message = clientPhone.messages.create(
                body='Person Detected',
                from_=config.FROM_NUMBER,
                to=config.TO_NUMBER
        )
        print(message.sid)
        person_detected=True
    count+=1

 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("test.mosquitto.org", 1883, 60)
 

client.loop_forever()