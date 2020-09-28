from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('user/register', views.register, name = 'register'),
    path('user/login', views.login, name = 'login'),
    path('user/logout', views.logout, name = 'logout'),
    path('user/profile', views.profile, name = 'profile'),
    path('user/profile/account', views.account, name = 'account'),
    path('user/profile/dashboard', views.dashboard, name = 'dashboard'),
    path('user/profile/dashboard/enrollments', views.courses_enrolled_in, name = 'courses_enrolled_in'),
    path('allcategories/<slug:category_name>/<slug:subcategory_name>/<slug:course_name>/<int:course_id>', views.enroll, name = 'enroll'),
    #path('user/dashboard/courses')
]