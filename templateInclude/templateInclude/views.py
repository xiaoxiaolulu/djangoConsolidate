from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def index1(request):
    return render(request, 'index1.html')