from django.http import HttpResponse
from django.shortcuts import render


# Create your views here
def book(request):
    return HttpResponse("图书首页")


def book_detail(request, book_id):
    return HttpResponse(book_id)
