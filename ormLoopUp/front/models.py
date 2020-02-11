from django.db import models


# Create your models here.
class Article(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title} {self.content} {self.category}"


class Category(models.Model):

    name = models.CharField(max_length=100)
