import memcache

mc = memcache.Client(["127.0.0.1:11211"], debug=True)
mc.set('username', 'helloworld', time=120)

# 设置多个值
mc.set_multi(
    {
        'title': 'hello',
        'age': '10'
    }
)

print(mc.get('username'))
mc.delete('username')
print(mc.get('username'))
