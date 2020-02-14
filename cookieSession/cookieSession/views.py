from datetime import datetime
from django.http import HttpResponse


def index(request):
    response = HttpResponse('index')
    expires = datetime(year=2019, month=2, day=14, hour=20, minute=0, second=0)
    # max_age=180
    # expires=expires
    response.set_cookie('username', 'hello', expires=expires)
    return response


def session_view(request):
    # request.session['username'] = 'hello'
    # username = request.session.get('username')
    # print(username)
    # request.session.pop('username')
    username = request.session.get('username')
    print(username)
    request.session.clear()

    # 设置过期时间
    request.session.set_expiry(10)
    return HttpResponse('session')
