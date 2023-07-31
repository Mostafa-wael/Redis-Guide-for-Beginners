import redis

# Connect to the Redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# LPUSH and RPUSH operations
redis_client.lpush('tasks', 'Task 3')
redis_client.lpush('tasks', 'Task 2')
redis_client.lpush('tasks', 'Task 1')

redis_client.rpush('tasks', 'Task 4')
redis_client.rpush('tasks', 'Task 5')

# LPOP and RPOP operations
task_1 = redis_client.lpop('tasks')
task_5 = redis_client.rpop('tasks')

print(task_1)  # Output: b'Task 1'
print(task_5)  # Output: b'Task 5'

# LRANGE operation
all_tasks = redis_client.lrange('tasks', 0, -1)
print(all_tasks)  # Output: [b'Task 2', b'Task 3', b'Task 4']
