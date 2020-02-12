from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from front.models import Book, Author, BookOrder, Publisher
from django.db.models import Avg, Count, Max, Min, Sum, F, Q, Prefetch
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


def index07(request):
    book = Book.objects.filter(price__gte=100, rating__gte=4.85)
    for boo in book:
        print(boo.name, boo.price, boo.rating)

    book1 = Book.objects.filter(Q(price__gte=100) & Q(rating__gte=4.85))
    for boo in book1:
        print(boo.name, boo.price, boo.rating)
    return HttpResponse('success')


def index08(request):
    print(type(Book.objects))
    from django.db.models.manager import Manager
    return HttpResponse('success')


def index09(request):
    # books = Book.objects.filter(id__gte=2)
    # print(type(books))
    # from django.db.models.query import QuerySet
    # b = books.filter(~Q(id=3))
    # for i in b:
    #     print(i.name)

    # book2 = Book.objects.filter(id__gte=2).exclude(id=3)
    # for b in book2:
    #     print(b)

    return HttpResponse('success')


def index10(request):
    # book_order = BookOrder.objects.order_by("create_time")
    # for book in book_order:
    #     print(book.id, book.price, book.create_time)
    #
    # books = BookOrder.objects.order_by("-create_time")
    # for book in books:
    #     print(book.id, book.price, book.create_time)

    # 根据时间和价格排序
    # books1 = BookOrder.objects.order_by("-create_time", "-price")
    # for book in books1:
    #     print(book.id, book.price, book.create_time)

    # 根据评分排序
    order = BookOrder.objects.order_by('book__rating')
    for o in order:
        print(o.id, o.book.rating)
    return HttpResponse('success')


def index11(request):
    # books = Book.objects.values("id", 'name')
    # print(type(books))
    # for book in books:
    #     print(book)
    #
    # book1 = Book.objects.values('author__name')
    # for b1 in book1:
    #     print(b1)

    # book = Book.objects.values('id', 'name', order_nums=Count('bookorder'))
    # for b in book:
    #     print(b)

    book = Book.objects.values_list('id', 'name')
    for b in book:
        print(b)
    return HttpResponse('success')


def index12(request):
    # books = Book.objects.all()
    # for book in books:
    #     print(book.author.name)

    books = Book.objects.select_related('author')
    for book in books:
        print(book.author.name)
    return HttpResponse('success')


def index13(request):
    # books = Book.objects.all()
    # for book in books:
    #     print(book.name)
    #     orders = book.bookorder_set.all()
    #     for order in orders:
    #         print(order.id)

    # books = Book.objects.prefetch_related('author')
    # for book in books:
    #     print(book.author, book.name)

    prefetch = Prefetch('bookorder_set', queryset=BookOrder.objects.filter(price__gte=90))
    books = Book.objects.prefetch_related(prefetch)
    for book in books:
        print(book.name)
        orders = book.bookorder_set.all()
        for order in orders:
            print(order.id)
    return HttpResponse('success')


def index14(request):
    # books = Book.objects.defer("name")
    # for book in books:
    #     print(book)

    books = Book.objects.only("name")
    for book in books:
        print(book.name)
    return HttpResponse('success')


def index15(request):
    # result = Publisher.objects.get_or_create(name="啊哈哈哈")
    # print(result)
    publisher = Publisher.objects.bulk_create(
        [
            Publisher(name='123132'),
            Publisher(name='2313213213')
        ]
    )
    print(publisher)
    return HttpResponse('success')