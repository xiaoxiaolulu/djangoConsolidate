from django.shortcuts import render


def greet(world):
    return 'hello world %s' % world


def index(request):
    context = {
        'greet': greet
    }
    return render(request, 'index.html')
