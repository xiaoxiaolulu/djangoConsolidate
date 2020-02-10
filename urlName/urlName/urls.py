"""urlName URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('font.urls')),
    # 同一个app下有两个实例
    # 指定实例命名空间，子url模块必须指定应用命名空间, 也可以在include中指定应用命名空间
    # include('cms.urls', 'cms'), namespace='cms1'

    # 传递列表 包含子模块路由传递
    # include([path('', view.movie), path('movie_list, view.move_list)'])

    path('cms1/', include('cms.urls'), namespace='cms1'),
    path('cms2/', include('cms.urls'), namespace='cms2')
]

