from django.db import models


# Create your models here.
class Author(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    class Meta:
        db_table = 'author'


class Publisher(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'publisher'


class Book(models.Model):

    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.FloatField()
    rating = models.FloatField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book'


class BookOrder(models.Model):

    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    price = models.FloatField()
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'book_order'
