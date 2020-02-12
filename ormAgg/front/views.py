from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from front.models import Book, Author, BookOrder
from django.db.models import Avg, Count, Max, Min, Sum, F
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


def index05(request):
    # book = BookOrder.objects.aggregate(total=Sum('price'))
    # print(book)
    #
    # order = Book.objects.annotate(total=Sum('bookorder__price'))
    # for o in order:
    #     print(o.name, o.total)

    book1 = BookOrder.objects.filter(create_time__year=2020).aggregate(total=Sum('price'))
    print(book1)
    print(connection.queries)

    order1 = Book.objects.filter(bookorder__create_time__year=2020).annotate(total=Sum('price'))
    for o in order1:
        print(o.name, o.total)

    return HttpResponse('success')


def index06(request):
    Book.objects.update(price=F('price')+10)
    print(connection.queries[-1])
    return HttpResponse('success')
