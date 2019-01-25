""""
soumil nitin shah
Bachelor in Electronic Engineering
Master in Electrical Engineering
Master in Computer Enginnering

shahsoumil519@gmail.com
https://github.com/soumilshah1995/IoT-Lab-2019

"""

# Import standard python modules.
import sys
import time
import random

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient


ADAFRUIT_IO_KEY = 'XXXXXXXXXXXXXX'
ADAFRUIT_IO_USERNAME = 'XXXXXX'
IO_FEED = 'XXXXXX'

def connected(client):
    print ('Connected to Adafruit IO! Listening for feed changes...')
    # subscribe to feed in a dashdoard
    client.subscribe('test')

def disconnected(client):
    print ('Disconnect from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):
    # feed_id or {0} represents the name of the feed in the message to the Adafruit IO service.
    # Payload or {1} represents the value being sent.
    print ('Feed {0} recieved new vaule: {1}'.format(feed_id, payload))

    if '{1}'.format(feed_id, payload) == "ON":
        print("ON Worked ")
    if '{1}'.format(feed_id, payload) == "OFF":
        print("OFF worked ")


client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.loop_background()
client.connect()

while 1:
    data = client.on_message


