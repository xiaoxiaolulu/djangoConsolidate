from django.core.cache import cache
from django.core.cache.backends.memcached import MemcachedCache
from django.http import HttpResponse


def index(request):
    cache.set('username', 'hello', 100)
    username = cache.get('username')
    print(username)
    return HttpResponse('success')
