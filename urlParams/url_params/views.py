from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def book(request):
    return HttpResponse("图书首页")


def book_detail(request, book_id):
    content = f"获取的book id 为：{book_id}"
    return HttpResponse(content)


def author_detail(request):
    author_id = request.GET.get('id')
    text = f"作者的id 是{author_id}"
    return HttpResponse(text)


def publisher_detail(request, publisher_id):
    text = f"出版社id是 {publisher_id}"
    return HttpResponse(text)
