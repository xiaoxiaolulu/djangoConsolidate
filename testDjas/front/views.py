from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission, ContentType, Group
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

# Create your views here.
from front.forms import LoginForm
from front.models import User, Article


def loginView(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = authenticate(request, username=telephone, password=password)
            if user and user.is_active:
                login(request, user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                return HttpResponse('登录成功')
            else:
                return HttpResponse('手机号或密码错误')
        else:
            print(form.errors)
            return redirect(reverse('login'))


@login_required(login_url='/login/')
def add(request):
    User.objects.create_user(telephone='13564957378', username='111', password='123456')
    return HttpResponse('手机号或密码错误')


def logoutView(request):
    logout(request)
    return HttpResponse("退出")


@permission_required('front.add_article', login_url='/login/', raise_exception=True)
def add_per(request):

    # content_type = ContentType.objects.get_for_model(Article)
    # permission = Permission.objects.create(codename='black_article', name='拉黑', content_type=content_type)

    # user = User.objects.first()
    # content_type = ContentType.objects.get_for_model(Article)
    # per = Permission.objects.filter(content_type=content_type)
    # for p in per:
    #     print(p)
    # user.user_permissions.set(per)
    # user.user_permissions.clear()
    # user.user_permissions.add(per[0])
    # user.user_permissions.remove(per[0])
    # if user.has_perm('front.view_article'):
    #     print("you")
    # else:
    #     print('mei')

    # if request.user.is_authenticated:
    #     print('登录ing')
    #     if request.user.has_perm('front.add_article'):
    #         return HttpResponse("马镫")
    #     else:
    #         return HttpResponse('没有访问页面权限', 403)
    # else:
    #     return redirect(reverse('login'))

    return HttpResponse("马镫")


def group(request):
    # group = Group.objects.create(name='测试')
    # content = ContentType.objects.get_for_model(Article)
    # permission = Permission.objects.filter(content_type=content)
    # group.permissions.set(permission)
    # group.save()

    # group = Group.objects.filter(name='测试').first()
    # user = User.objects.first()
    # user.groups.add(group)
    # user.save()
    user = User.objects.first()
    print(user.get_group_permissions())
    return HttpResponse('分组成功')