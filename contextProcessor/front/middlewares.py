from front.models import User


def front_user_middleware(get_response):

    def middleware(request):
        print("request到达view之前执行的代码")
        user_id = request.session.get('user_id')
        try:
            user = User.objects.get(pk=user_id)
            request.front_user = user
        except User.DoesNotExist:
            request.front_user = None
        response = get_response(request)
        print("response到达浏览器之前执行的代码")
        return response

    return middleware


class FrontUserMiddleware(object):

    def __init__(self, get_response):
        print("初始化代码")
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        print("request到达view之前执行的代码")
        user_id = request.session.get('user_id')
        try:
            user = User.objects.get(pk=user_id)
            request.front_user = user
        except User.DoesNotExist:
            request.front_user = None
        response = self.get_response(request)
        print("response到达浏览器之前执行的代码")
        return response

from django.utils.deprecation import MiddlewareMixin


class FrontUserMiddlewareMixin(MiddlewareMixin):

    def __init__(self, get_response):
        super(FrontUserMiddlewareMixin, self).__init__(get_response)

    def process_request(self, request):
        print("request到达view之前执行的代码")
        user_id = request.session.get('user_id')
        try:
            user = User.objects.get(pk=user_id)
            request.front_user = user
        except User.DoesNotExist:
            request.front_user = None

    def process_response(self, request, response):
        # response = self.get_response(request)
        print("response到达浏览器之前执行的代码")
        return response

from django.middleware.security import SecurityMiddleware
from django.middleware.gzip import GZipMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.middleware.common import CommonMiddleware
from django.middleware.csrf import CsrfViewMiddleware
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.contrib.messages.middleware import MessageMiddleware
from django.middleware.clickjacking import XFrameOptionsMiddleware