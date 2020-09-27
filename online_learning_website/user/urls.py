from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('user/register', views.register, name = 'register'),
    path('user/login', views.login, name = 'login'),
    path('user/logout', views.logout, name = 'logout'),
    path('user/dashboard', views.dashboard, name = 'dashboard')
]