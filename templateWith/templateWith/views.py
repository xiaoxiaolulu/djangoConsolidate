from django.shortcuts import render


def index(request):
    context = {
        'person': [1, 2, 3, 4, 5]
    }
    return render(request, 'index.html', context=context)