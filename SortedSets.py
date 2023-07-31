import redis

# Connect to the Redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# ZADD operation
redis_client.zadd('scores', {'Alice': 90, 'Bob': 85, 'John': 78})

# ZRANGE operation
top_scores = redis_client.zrange('scores', 0, -1, withscores=True)
print(top_scores)  # Output: [(b'John', 78.0), (b'Bob', 85.0), (b'Alice', 90.0)]

# ZSCORE operation
alice_score = redis_client.zscore('scores', 'Alice')
print(alice_score)  # Output: 90.0

# ZREM operation
redis_client.zrem('scores', 'John')
print(redis_client.zrange('scores', 0, -1, withscores=True))  # Output: [(b'Bob', 85.0), (b'Alice', 90.0)]