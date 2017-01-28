import sys
import redis

conn = redis.Redis()

keys = conn.keys('*')

vals = conn.mget(keys)

n = 0

for val in vals:
    if val == b'Japan':
        print(val)
        n += 1

print(n)
