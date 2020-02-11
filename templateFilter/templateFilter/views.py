from django.shortcuts import render


def greet(world):
    return 'hello world %s' % world


def index(request):
    # context = {
    #     'greet': greet
    # }
    # import datetime
    # context = {
    #     'today': datetime.datetime.now()
    # }
    context = {
        'value': ''
    }
    return render(request, 'index.html', context=context)
