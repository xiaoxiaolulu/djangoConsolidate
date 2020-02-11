from django.shortcuts import render


class Person:

    def __init__(self, username):
        self.username = username


def index(request):
    p = Person("脑残")
    context = {
        'person': [
            "1"
        ]
        # 'person': {
        #     "username": "弱鸡",
        #     "keys": "hello world"
        # }
    }
    return render(request, 'index.html', context=context)