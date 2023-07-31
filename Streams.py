import redis

# Connect to the Redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# XADD operation
message_id = redis_client.xadd('stream1', {'name': 'Alice', 'age': 30})
print(message_id)  # Output: b'1630429723087-0'

# XLEN operation
stream_length = redis_client.xlen('stream1')
print(stream_length)  # Output: 1

# XREAD operation
messages = redis_client.xread(count=1, streams={'stream1': '0'})
print(messages)  # Output: {b'stream1': [(b'1630429723087-0', {b'name': b'Alice', b'age': b'30'})]}

# XGROUP CREATE operation
group_created = redis_client.xgroup_create('stream1', 'consumer_group1', id='0', mkstream=True)
print(group_created)  # Output: True

# XREADGROUP operation
messages_group = redis_client.xreadgroup('consumer_group1', 'consumer1', count=1, streams={'stream1': '>'})
print(messages_group)  # Output: {b'stream1': [(b'1630429723087-0', {b'name': b'Alice', b'age': b'30'})]}

# XACK operation
message_id = b'1630429723087-0'
redis_client.xack('stream1', 'consumer_group1', message_id)

# XREADGROUP to check if the message is not pending anymore
messages_group = redis_client.xreadgroup('consumer_group1', 'consumer1', count=1, streams={'stream1': '>'})
print(messages_group)  # Output: {}
