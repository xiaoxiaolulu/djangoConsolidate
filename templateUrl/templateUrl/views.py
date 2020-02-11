from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    
    return render(request, 'index.html')


def book(request):
    return HttpResponse('1')


def book2(request):
    return HttpResponse('2')


def book3(request):
    return HttpResponse('3')


def book4(request):
    return HttpResponse('4')


def book_detail(request, book_id):
    return HttpResponse(book_id)