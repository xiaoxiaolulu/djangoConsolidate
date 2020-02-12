from django.db import models


# Create your models here.
class Article(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)


class Category(models.Model):

    name = models.CharField(max_length=100)
