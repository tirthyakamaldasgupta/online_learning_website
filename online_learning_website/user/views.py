from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import sessions, messages, auth
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, AccountDetailsForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import AdditionalStudentDetail, AdditionalInstructorDetail
from course.models import Course, Enrollment

def register(request):
    if request.method == "POST":
        userregistrationform = UserRegisterForm(request.POST)
        if userregistrationform.is_valid():
            userregistrationform.save()
            username = userregistrationform.cleaned_data['username']
            user = User.objects.get(username = username)
            if userregistrationform.cleaned_data['type_of_users'] == '1':
                addadditionalstudentdetails = AdditionalStudentDetail(user = user)
                addadditionalstudentdetails.save()
                reg_successful_message = 'Hello, ' + user.first_name + ' ' + user.last_name + ', thanks for choosing our platform to enhance your learning experience!'
                messages.success(request, reg_successful_message)
            elif userregistrationform.cleaned_data['type_of_users'] == '2':
                addadditionalinstructordetails = AdditionalInstructorDetail(user = user)
                addadditionalinstructordetails.save()
                reg_successful_message = 'Hello, ' + user.first_name + ' ' + user.last_name + ', great to have you onboard as an instructor!'
                messages.success(request, reg_successful_message)
            return redirect('login')
    else:
        userregistrationform = UserRegisterForm()
    return render(request, 'user/user_register.html', {'userregistrationform' : userregistrationform})

def login(request):
    if request.method == "POST":
        userloginform = AuthenticationForm(request, request.POST)
        if userloginform.is_valid():
            username = userloginform.cleaned_data.get('username')
            password = userloginform.cleaned_data.get('password')
            next = request.POST['next']
            user = auth.authenticate(username = username, password = password)
            if user is not None:
                auth.login(request, user)
                if next:
                    return redirect(next)
                else:
                    return redirect('/user/profile')
            else:
                messages.error(request, 'Wrong username or password provided!')
        else:
            messages.error(request, 'Wrong username or password provided!')
    userloginform = AuthenticationForm()
    return render(request, 'user/user_login.html', {'userloginform' : userloginform})

def logout(request):
    auth.logout(request)
    logout_successful_message = 'You have logged out successfully!'
    messages.success(request, logout_successful_message)
    return redirect('/')

def profile(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'user/user_profile.html', {'user' : user})

def account(request):
    user = request.user
    accountdetailsform = AccountDetailsForm()
    if user.is_authenticated:
        return render(request, 'user/user_account.html', {'user' : user, 'accountdetailsform' : accountdetailsform})
    #return render(request, 'user/user_account.html')

def dashboard(request):
    user = request.user
    if user.is_authenticated:
        if hasattr(user, 'additionalstudentdetail') == True:
            return render(request, 'user/student_dashboard.html', {'user' : user})
        elif hasattr(user, 'additionalinstructordetail') == True:
            return render(request, 'user/instructor_dashboard.html', {'user' : user})

def courses_enrolled_in(request):
    user = request.user
    if user.is_authenticated:
        if hasattr(user, 'additionalstudentdetail') == True:
            enrollments = user.additionalstudentdetail.enrollment_set.all()
            return render(request, 'user/courses_enrolled_in.html', {'enrollments' : enrollments})

@login_required
def enroll(request, category_name, subcategory_name, course_name, course_id):
    user = request.user
    if user.is_authenticated:
        if hasattr(user, 'additionalstudentdetail') == True:
            enrollment_count = Enrollment.objects.filter(student_id = user.additionalstudentdetail, course_id = Course.objects.get(id = course_id)).count()
            if enrollment_count == 0:
                new_enrollment = Enrollment(student_id = user.additionalstudentdetail, course_id = Course.objects.get(id = course_id))
                new_enrollment.save()
                return redirect('/user/profile/dashboard/enrollments')
            else:
                messages.error(request, 'You are already enrolled!')
                return HttpResponseRedirect(reverse('view_course', args=(category_name, subcategory_name, course_name)))          