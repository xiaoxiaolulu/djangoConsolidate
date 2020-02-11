from django.db import models


# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=200)


class UserExtension(models.Model):

    school = models.CharField(max_length=200)
    # 外键必须保持唯一 (一对一外键)
    # kwargs['unique'] = True
    user = models.OneToOneField('User', on_delete=models.CASCADE)