from django.urls import path
from font import views

# 应用命名空间
app_name = 'font'

urlpatterns = [
    path('', views.index),
    path('login/', views.login)
]
