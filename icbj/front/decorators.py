from front.models import User
from django.shortcuts import redirect, reverse


def login_required(func):

    def wrapper(request, *args, **kwargs):
        exists = request.front_user
        if exists:
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('login'))

    return wrapper
