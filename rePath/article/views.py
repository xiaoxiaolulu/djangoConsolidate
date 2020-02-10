from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def article(request):
    return HttpResponse("文章首页")


def article_list(request, year):
    return HttpResponse(f"文章列表 -> {year}")


def article_list_month(request, month):
    return HttpResponse(f"文章列表 -> {month}")
