from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from front.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
from django.views.generic import View

from front.forms import RegisterForm, LoginForm, TransForm
from front.models import User


def index(request):
    return render(request, 'index.html')


class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(email=email, password=password).first()
            if user:
                request.session['user_id'] = user.pk
                return redirect(reverse('index'))
            else:
                return redirect(reverse('login'))
        else:
            print(form.errors)
            return redirect(reverse('login'))


class Register(View):
    
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            User.objects.create(email=email, password=password, username=username, balance=1000)
            return redirect(reverse('login'))
        else:
            print(form.errors)
            return redirect(reverse('register'))


@method_decorator(login_required, name='dispatch')
class Transfer(View):
    
    def get(self, request):
        return render(request, 'transfer.html')

    def post(self, request):
        form = TransForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            money = form.cleaned_data.get('money')
            # user_id = request.session.get('user_id')
            user = request.front_user
            if user.balance >= money:
                User.objects.filter(email=email).update(balance=F('balance') + money)
                user.balance -= money
                user.save()
                return HttpResponse('转账成功')
            else:
                return HttpResponse('转账失败')
        else:
            print(form.errors)
            return redirect(reverse('transfer'))


def logout(request):
    request.session.flush()
    return redirect(reverse('index'))
