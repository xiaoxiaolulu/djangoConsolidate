from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    # ?username
    username = request.GET.get('username')
    if username:
        return HttpResponse("font首页")
    else:
        # 路由反转
        # return redirect(reverse('login'))
        # 根据应用命名空间反转路由
        return redirect(reverse('cms:login'))


def login(request):
    return HttpResponse("font登录")
