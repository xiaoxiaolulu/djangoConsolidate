from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def index01(request):
    return render(request, 'index01.html')


def index02(request):
    return render(request, 'index02.html')