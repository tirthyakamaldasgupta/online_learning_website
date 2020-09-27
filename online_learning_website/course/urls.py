from django.urls import path, include
from . import views

urlpatterns = [
    path('allcategories/', views.all_categories, name = 'all_categories'),
    path('allcategories/<slug:category_name>/', views.all_subcategories, name = 'all_subcategories'),
    path('allcategories/<slug:category_name>/<slug:subcategory_name>/', views.all_courses_preview, name = 'all_courses_preview'),
    path('allcategories/<slug:category_name>/<slug:subcategory_name>/<slug:course_name>/', views.view_course, name = 'view_course'),
]