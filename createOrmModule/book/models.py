from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    price = models.FloatField(null=False, default=0)

# python  manage.py makemigrations
# python manage.py migrate


class Publisher(models.Model):
    
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
