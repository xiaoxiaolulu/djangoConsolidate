from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def book(request):
    """
    视图函数第一个参数必须是request
    返回值必须是HttpResponseBase的子类对象
    :param request:
    :return:
    """
    return HttpResponse("图书首页")
