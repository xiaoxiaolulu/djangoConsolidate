from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from front.models import Book, Author
from django.db.models import Avg, Count, Max, Min
from django.db import connection


def index(request):
    # 'SELECT AVG(`book`.`price`) AS `price__avg` FROM `book`
    # 别名 price_avg=Avg('price')
    result = Book.objects.aggregate(price_avg=Avg('price'))
    print(result)
    print(connection.queries)
    return HttpResponse('success')


def index02(request):
    # 每本书的平均销售价格
    # annotate 增加了order_by进行分组
    result = Book.objects.annotate(avg=Avg('bookorder__price'))
    for book in result:
        print(book.name, book.avg)
    print(connection.queries)
    return HttpResponse('success')


def index03(request):
    # res = Book.objects.aggregate(book_nums=Count("id"))
    # print(res)
    # print(connection.queries)
    # 
    # res1 = Author.objects.aggregate(email_nums=Count('email', distinct=True))
    # print(res1)
    # print(connection.queries)

    books = Book.objects.annotate(book_nums=Count('bookorder'))
    for book in books:
        print(book.name, book.book_nums)
    print(connection.queries)
    # SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`,
    # `book`.`publisher_id`, COUNT(`book_order`.`id`) AS `book_nums` FROM `book` LEFT OUTER JOIN `book_order` ON
    # (`book`.`id` = `book_order`.`book_id`) GROUP BY `book`.`id` ORDER BY NULL
    return HttpResponse('success')


def index04(request):
    author = Author.objects.aggregate(max=Max('age'), min=Min('age'))
    print(author)
    print(connection.queries)

    books = Book.objects.annotate(max=Max('bookorder__price'), min=Min('bookorder__price'))
    for book in books:
        print(book.name, book.min, book.max)
    return HttpResponse('success')