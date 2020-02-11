from django.shortcuts import render


def index(request):
    # context = {
    #     'age': 18
    # }
    context = {
        'heros': [
            "1",
            "2", 
            "3"
        ]
    }
    return render(request, 'index.html', context=context)