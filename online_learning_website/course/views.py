from django.shortcuts import render
from django.utils.text import slugify
from .models import Category, SubCategory, Course
from user.views import AdditionalStudentDetail, Enrollment

#For viewing the categories of courses.
def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'course/all_categories.html', {'categories' : categories})

#For viewing the subcategories of each categories of courses.
def all_subcategories(request, category_name):
    category = Category.objects.get(slug = category_name)
    subcategories = category.subcategory_set.all
    return render(request, 'course/all_subcategories.html', {'category' : category, 'subcategories' : subcategories})

#For viewing the courses listed with each subcategory.
def all_courses_preview(request, category_name, subcategory_name):
    subcategory = SubCategory.objects.get(slug = subcategory_name)
    courses_by_subcategory = subcategory.course_set.all()
    return render(request, 'course/all_courses_preview.html', {'category_name' : category_name, 'subcategory_name' : subcategory.name, 'courses_by_subcategory' : courses_by_subcategory})

#For viewing a particular course.
def view_course(request, category_name, subcategory_name, course_name):
    user = request.user
    course = Course.objects.get(slug = course_name)
    enrollment_count = Enrollment.objects.filter(student_id = user.additionalstudentdetail, course_id = course).count()
    return render(request, 'course/course.html', {'category_name' : category_name, 'subcategory_name' : subcategory_name, 'course' : course, 'enrollment_count' : enrollment_count})