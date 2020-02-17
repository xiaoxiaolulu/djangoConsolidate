
from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth.models import User

# Create your views here.
# from front.models import Person
# 
# 
# def index(request):
#     user = User.objects.create_user(username='hello', email='546462@qq.com', password='111111')
#     # 超级用户
#     User.objects.create_superuser(username='world', email='213216@qq.com', password='222222')
#     
#     from django.contrib.auth import authenticate
#     username = 'hello'
#     password = '111111'
#     user = authenticate(request, username=username, password=password)
#     if user:
#         pass
#     else:
#         pass
#     return HttpResponse('success')
# 
# 
# def proxy_view(request):
# 
#     blacklist = Person.get_blacklist()
#     for p in blacklist:
#         print(p.username)
#     return HttpResponse('success')
# 
# 
# def my_authenticate(telephone, password):
#     user = User.objects.filter(telephone=telephone).first()
#     if user:
#         is_correct = user.check_password(password)
#         if is_correct:
#             return user
#         else:
#             return None
#     else:
#         return None
# 
# 
# def one_view(request):
#     user = User.objects.create_user(username='1121', email='21311@qq.com', password='12313')
#     user.extension.telephone = '13564957378'
#     user.save()
# 
#     user = my_authenticate(telephone='13564957378', password='12313')
# 
#     return HttpResponse('success')
# from front.models import User
#
#
# def extend(request):
#
#     User.objects.create_user(telephone='13564957378', username='12321', password='123456')
#     return HttpResponse('success')


