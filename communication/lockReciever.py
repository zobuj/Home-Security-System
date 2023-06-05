#recieves a message at the lock and will be used to send signal to open door
 
import paho.mqtt.client as mqtt
 

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 

    
    client.subscribe("CoreElectronics/sender")
 

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()