from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.all_courses_preview_by_various_filters, name = 'all_courses_preview_by_various_filters')
]