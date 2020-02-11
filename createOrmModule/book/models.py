from django.db import models


# Create your models here.
from django.utils import timezone


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    price = models.FloatField(null=False, default=0)

    def __str__(self):
        return f"{self.id} {self.name} {self.author} {self.price}"

# python  manage.py makemigrations
# python manage.py migrate


class Publisher(models.Model):
    
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)


class Article(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    # removed = models.BooleanField(default=1)
    create_time = models.DateTimeField(default=timezone.now)
