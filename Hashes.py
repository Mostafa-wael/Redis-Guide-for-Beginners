import redis

# Connect to the Redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# HSET and HGET operations
redis_client.hset('user:1', 'name', 'Alice')
redis_client.hset('user:1', 'age', 30)

name = redis_client.hget('user:1', 'name')
age = redis_client.hget('user:1', 'age')

print(name)  # Output: b'Alice'
print(age)   # Output: b'30'

# HMSET and HGETALL operations
user_data = {'name': 'Bob', 'age': 25, 'country': 'USA'} # dict
redis_client.hmset('user:2', user_data)

user_info = redis_client.hgetall('user:2')
print(user_info)  # Output: {b'name': b'Bob', b'age': b'25', b'country': b'USA'}
