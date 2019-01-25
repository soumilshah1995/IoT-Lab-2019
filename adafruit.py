
# Import library and create instance of REST client.
from Adafruit_IO import *
from Adafruit_IO import Client

# importing AIO key and username
aio = Client('USERNAME', 'CLIENT_AIO')

# Add the value 98.6 to the feed 'Temperature'.
soumil = aio.feeds('soumil')
aio.send_data(soumil.key, 98.6)

# Receiving Data from  server
data = aio.receive('soumil')
print('Received value: {0}'.format(data.value))

# Get list of feeds.
feeds = aio.feeds()

# Print out the feed names:
for f in feeds:
    print('Feed: {0}'.format(f.name))

"""
# Create Feed object with name 'Foo'.
feed = Feed(name='Foo')

# Send the Feed to IO to create.
# The returned object will contain all the details about the created feed.
result = aio.create_feed(feed)

# Delete the feed with name 'Test'.
aio.delete_feed('Test')


"""