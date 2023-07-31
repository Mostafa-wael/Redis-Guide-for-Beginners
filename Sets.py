import redis

# Connect to the Redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# SADD operation
redis_client.sadd('fruits', 'apple')
redis_client.sadd('fruits', 'banana')
redis_client.sadd('fruits', 'orange')

# SMEMBERS operation
all_fruits = redis_client.smembers('fruits')
print(all_fruits)  # Output: {b'orange', b'banana', b'apple'} (order may vary)

# SISMEMBER operation
print(redis_client.sismember('fruits', 'apple'))  # Output: True
print(redis_client.sismember('fruits', 'grapes'))  # Output: False

# SREM operation
redis_client.srem('fruits', 'banana')
print(redis_client.smembers('fruits'))  # Output: {b'orange', b'apple'}

# SINTER operation
redis_client.sadd('vegetables', 'carrot')
redis_client.sadd('vegetables', 'potato')

intersection = redis_client.sinter('fruits', 'vegetables')
print(intersection)  # Output: set()