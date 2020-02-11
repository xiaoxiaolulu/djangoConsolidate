from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=100)


class Article(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='articles')
    # 
    # def __str__(self):
    #     return f"{self.title}  {self.content} {self.category}"


class Tag(models.Model):

    name = models.CharField(max_length=100)
    article = models.ManyToManyField('Article')
