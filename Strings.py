import redis # pip install redis

# Connect to the Redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# SET and GET operations
redis_client.set('name', 'John')
name = redis_client.get('name')
print(name)  # Output: b'John' (Note: Redis returns bytes, not strings directly)

# INCR and DECR operations
redis_client.set('counter', 10)
redis_client.incr('counter')
counter_value = redis_client.get('counter')
print(counter_value)  # Output: b'11'