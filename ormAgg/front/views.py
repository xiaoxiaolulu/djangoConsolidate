from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from front.models import Book
from django.db.models import Avg
from django.db import connection


def index(request):
    # 'SELECT AVG(`book`.`price`) AS `price__avg` FROM `book`
    # 别名 price_avg=Avg('price')
    result = Book.objects.aggregate(price_avg=Avg('price'))
    print(result)
    print(connection.queries)
    return HttpResponse('success')