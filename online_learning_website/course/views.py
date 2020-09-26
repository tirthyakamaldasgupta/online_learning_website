from django.shortcuts import render
from .models import Category

def all_courses_preview_by_various_filters(request):
    categories = Category.objects.all()
    #subcategory_list = []
    #for category in categories:
        #subcategories = category.subcategory_set.all()
        #subcategory_lists.append(subcategories)

    return render(request, 'course/all_courses_preview_by_various_filters.html', {'categories' : categories})   
