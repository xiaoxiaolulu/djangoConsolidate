from django.db import models

# Create your models here.


class User(models.Model):

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)
    balance = models.FloatField()
    