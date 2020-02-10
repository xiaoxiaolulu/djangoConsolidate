from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def article(request):

    return HttpResponse("文章首页")


def article_list(request, categories):
    return HttpResponse(categories)
