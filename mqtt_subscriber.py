"""MQTT subscriber example."""

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected to local broker successfully.")
    client.subscribe("test/helloworld")

def on_message(client, userdata, msg):
    print(f"Received local message: {msg.payload.decode()} on topic {msg.topic}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="local_subscriber")
client.on_connect = on_connect
client.on_message = on_message

# Connect to your local broker on the default port 1883
client.connect("localhost", 1883, 60)

client.loop_forever()
