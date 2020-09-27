from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import sessions, messages, auth
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import AdditionalStudentDetail, AdditionalInstructorDetail

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
            elif userregistrationform.cleaned_data['type_of_users'] == '2':
                addadditionalinstructordetails = AdditionalInstructorDetail(user = user)
                addadditionalinstructordetails.save()
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
            user = auth.authenticate(username = username, password = password)
            if user is not None:
                auth.login(request, user)
                return redirect('/user/profile')
            else:
                messages.error(request, 'Wrong username or password provided!')
        else:
            messages.error(request, 'Wrong username or password provided!')
    userloginform = AuthenticationForm()
    return render(request, 'user/user_login.html', {'userloginform' : userloginform})

def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'user/user_profile.html', {'user' : user})

def account(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'user/user_account.html', {'user' : user})

def dashboard(request):
    user = request.user
    if user.is_authenticated:
        if hasattr(user, 'additionalstudentdetail') == True:
            return render(request, 'user/student_dashboard.html', {'user' : user})
        elif hasattr(user, 'additionalinstructordetail') == True:
            return render(request, 'user/instructor_dashboard.html', {'user' : user})
    

