# URL分层模块化
from django.urls import path
from urlIncluding import views


urlpatterns = [
    path('', views.book),
    path('book/<book_id>', views.book_detail)
]