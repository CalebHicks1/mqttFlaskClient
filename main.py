import paho.mqtt.client as mqtt
import time
#########################################################
def on_message(client, userdata, message):
    print("message recieved", str(message.payload.decode("utf-8")))
#########################################################

# Initialize the client object.
client = mqtt.Client()
client.on_message=on_message
# Connect to the broker
host = "broker.emqx.io"
client.connect(host)

client.loop_start()
client.subscribe("test")
# Publish message
client.publish("test","112345")
time.sleep(4)
client.loop_stop()
