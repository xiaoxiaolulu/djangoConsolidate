from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from user.models import User, UserExtension


def one_to_one_view(request):

    # user = User.objects.first()
    # ex = UserExtension(school='1231')
    # ex.user = user
    # ex.save()

    user = User.objects.first()
    print(user.userextension)
    return HttpResponse("success")