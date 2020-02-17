from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.


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
        
        
class User(AbstractBaseUser, PermissionsMixin):
    telephone = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = []
    objects = UserManage()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username