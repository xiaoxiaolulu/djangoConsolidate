from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("cms首页")


def login(request):
    return HttpResponse("cms登录")