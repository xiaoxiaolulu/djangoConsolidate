from django.db import models
from django.core import validators


# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=100)
    telephone = models.CharField(max_length=11)
    password = models.CharField(max_length=11, null=True)


class Book(models.Model):

    title = models.CharField(max_length=100)
    page = models.IntegerField()
    price = models.FloatField(validators=[validators.MaxValueValidator(limit_value=1000)])


class Article(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    # thumbnial = models.FileField(upload_to='files')
    thumbnial = models.FileField(upload_to='%Y/%m/%d', validators=[validators.FileExtensionValidator(['txt', 'png'])])
