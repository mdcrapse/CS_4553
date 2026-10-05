#129.101.132.193

import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="local_publisher")

# Connect to your local broker on the default port 1883
client.connect("localhost", 1883, 60)

topic = "test/helloworld"
message = "Hello World from localhost!"

client.publish(topic, message)
print(f"Published '{message}' to {topic}")

client.disconnect()
