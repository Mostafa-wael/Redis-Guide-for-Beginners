import redis
import threading

def subscribe_to_channel(channel):
    # Connect to the Redis server for subscribing
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
    pub_sub = redis_client.pubsub()
    pub_sub.subscribe(channel)

    for message in pub_sub.listen():
        if message['type'] == 'message':
            print(f"Received message from {channel}: {message['data'].decode('utf-8')}")

def publish_to_channel(channel, message):
    # Connect to the Redis server for publishing
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
    redis_client.publish(channel, message)

# In a real scenario, these two operations will run in different threads or processes.
# For simplicity, let's run them sequentially in the main thread.

# Subscribe to a channel (Run this first before publishing)
subscription_thread = threading.Thread(target=subscribe_to_channel, args=('my_channel',))
subscription_thread.start()

# Wait for a short time to make sure the subscriber is ready before publishing
subscription_thread.join(timeout=1)

# Publish a message to the channel
publish_to_channel('my_channel', 'Hello, Redis Pub/Sub!')

# Make sure the program waits for the subscriber to receive the message
subscription_thread.join()