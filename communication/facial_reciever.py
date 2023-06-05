#Collects the tensor for the facial recognition and compares it to the database, must be run in the new env

import facial_sender
import paho.mqtt.client as mqtt
import ast

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("CoreElectronics/facialReciever")

def on_message(client, userdata, msg):

    tensor = msg.payload.decode('utf-8')[2:-2].split()
    tensor = [float(x) for x in tensor]

    facial_sender.compareDatabase(tensor)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("test.mosquitto.org", 1883, 60)
 

client.loop_forever()