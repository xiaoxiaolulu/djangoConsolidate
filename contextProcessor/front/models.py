from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class User(models.Model):

    username = models.CharField(max_length=100, validators=[MinLengthValidator(4)])
    password = models.CharField(max_length=16, validators=[MinLengthValidator(6)])
    telephone = models.CharField(max_length=11)
