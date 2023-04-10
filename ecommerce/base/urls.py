from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.user_login, name="user_login"),
    path('register', views.user_register, name="user_register"),
    path('user', views.user_page, name="user_page"),
    path('logout', views.user_logout, name="user_logout"),
    path('recover', views.password_reset, name="password_reset"),
]