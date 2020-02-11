from django.shortcuts import render


# Create your views here.
from django.utils.timezone import now, localtime

from book.models import Book, Article


def index(request):
    # 添加一条数据
    # book = Book(name="桑果演绎", author='jack', price=200)
    # book.save()

    # 查询
    # book = Book.objects.get(pk=1)
    # print(book)
    #
    # book1 = Book.objects.filter(name='桑果演绎')
    # print(book1)
    # print(book1.first())

    # 删除
    # book = Book.objects.get(pk=1)
    # book.delete()

    # 修改
    # book = Book.objects.get(pk=1)
    # book.price = 3000
    # book.save()

    article = Article(create_time=now())
    article.save()
    return render(request, 'index.html')
