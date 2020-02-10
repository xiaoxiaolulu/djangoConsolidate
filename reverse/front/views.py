from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse("首页")
    else:
        # return redirect(reverse('login'))
        # 传递关键字参数
        # return redirect(reverse('detail', kwargs={'article_id': 1}))
        login_url = reverse('login') + "?next=/"
        return redirect(login_url)


def login(request):
    return HttpResponse("登录页面")


def article_detail(request, article_id):
    return HttpResponse(article_id)
