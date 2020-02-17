from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Person(User):
       
    class Meat:
        
        proxy = True
    
    @classmethod
    def get_blacklist(cls):
        return cls.objects.filter(is_active=False)
