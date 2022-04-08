import time
import paho.mqtt.client as mqtt_client
import random

broker="broker.emqx.io"

def on_message(client, userdata, message):
    time.sleep(1)
    data = str(message.payload.decode("utf-8"))
    print("received message =", data)
    
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

client= mqtt_client.Client(f'lab_{random.randint(10000, 99999)}') 
client.on_message=on_message
client.on_connect=on_connect

client.connect(broker) 
client.loop_start() 
print("Subcribing")
client.subscribe("lab/debug/led_state")
time.sleep(1800)
client.disconnect()
client.loop_stop()
