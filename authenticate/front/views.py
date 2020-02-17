from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from front.models import Person


def index(request):
    user = User.objects.create_user(username='hello', email='546462@qq.com', password='111111')
    # 超级用户
    User.objects.create_superuser(username='world', email='213216@qq.com', password='222222')
    
    from django.contrib.auth import authenticate
    username = 'hello'
    password = '111111'
    user = authenticate(request, username=username, password=password)
    if user:
        pass
    else:
        pass
    return HttpResponse('success')


def proxy_view(request):

    blacklist = Person.get_blacklist()
    for p in blacklist:
        print(p.username)
    return HttpResponse('success')