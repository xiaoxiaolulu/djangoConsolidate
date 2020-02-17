
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.models import User
#
# # Create your models here.
#
#
# class Person(User):
#
#     class Meat:
#
#         proxy = True
#
#     @classmethod
#     def get_blacklist(cls):
#         return cls.objects.filter(is_active=False)
#
#
# class UserExtension(models.Model):
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extension')
#     telephone = models.CharField(max_length=11)
#     school = models.CharField(max_length=100)
#
#
# from django.dispatch import receiver
# from django.db.models.signals import post_save
#
#
# @receiver(post_save, sender=User)
# def handler_user_extension(sender, instance, created, **kwargs):
#
#     if created:
#         UserExtension.objects.create(user=instance)
#     else:
#         instance.extension.save()
#
#
# from django.contrib.auth.models import AbstractUser


class UserManage(BaseUserManager):

    def _create_user(self, telephone, username, password, **kwargs):
        if not telephone:
            raise ValueError('必须传递手机号码')
        if not password:
            raise ValueError('必须传递密码')
        user = self.model(telephone=telephone, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, telephone, username, password, **kwargs):
        kwargs['is_superuser'] = False
        self._create_user(telephone, username, password, **kwargs)

    def create_superuser(self, telephone, username, password, **kwargs):
        kwargs['is_superuser'] = True
        self._create_user(telephone, username, password, **kwargs)

# 
# class User(AbstractUser):
# 
#     telephone = models.CharField(max_length=11, unique=True)
#     school = models.CharField(max_length=100)
# 
#     USERNAME_FIELD = 'telephone'
#     objects = UserManage()



