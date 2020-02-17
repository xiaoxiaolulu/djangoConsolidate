from redis import Redis


cache = Redis(host='127.0.0.1', port=6379)

# cache.set("username", 'hello')
# print(cache.get('username'))
# cache.delete('username')


# cache.rpush('languanges', 'java')
# print(cache.lrange('languanges', 0, -1))


# cache.sadd('team', 'li')
# print(cache.smembers('team'))

# cache.hset('web', 'name', 'www')
# print(cache.hget('web', 'name'))

# pip = cache.pipeline()
# pip.set('username1', 'w')
# pip.execute()

ps = cache.pubsub()
ps.subscribe('email')
while True:
    for item in ps.listen():
        print(item)
