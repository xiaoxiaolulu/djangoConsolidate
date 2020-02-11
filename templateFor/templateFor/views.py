from django.shortcuts import render


def index(request):
    context = {
       'book': [1, 2, 3, 4, 5, 6, 7, 8],
       'person': {
            'username': '123',
            'age':  12
        }
    }
    return render(request, 'index.html', context=context)
