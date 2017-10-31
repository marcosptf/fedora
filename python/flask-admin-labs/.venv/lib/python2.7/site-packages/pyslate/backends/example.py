#!/bin/python

import redis
from redis_backend import RedisBackend

r = redis.StrictRedis(host='localhost', port=6379, db=0)

b = RedisBackend(r, prefix="")

print(b.get_record(["john"], ["pl", "en"]))