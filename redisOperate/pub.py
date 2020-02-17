from redis import Redis


cache = Redis(host='127.0.0.1', port=6379)

for x in range(3):
    cache.publish('email', 'xxxQQ@qq.com')