from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

types_of_users_list = [('1', 'Student'), ('2', 'Instructor')]

class UserRegisterForm(forms.Form):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    email = forms.EmailField(required = True)
    confirm_email = forms.EmailField(required = True)
    username = forms.CharField(required = True)
    password = forms.CharField(required = True, widget=forms.PasswordInput)
    confirm_password = forms.CharField(required = True, widget=forms.PasswordInput)
    type_of_users = forms.ChoiceField(label = 'Who are you? *', required = True, choices = types_of_users_list)
    
    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username = username)
        if user.count():
            raise ValidationError("Username already exists!")
        return username

    def clean_confirm_email(self):
        email = self.cleaned_data['email'].lower()
        confirm_email = self.cleaned_data['confirm_email'].lower()
        user = User.objects.filter(email = email)
        if user.count():
            raise ValidationError("Email already exists!")
        return confirm_email

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords must match!")
        return confirm_password
    
    def save(self, commit = True):
        user = User.objects.create_user(first_name = self.cleaned_data['first_name'], last_name = self.cleaned_data['last_name'], email = self.cleaned_data['email'], username = self.cleaned_data['username'], password = self.cleaned_data['password'])
        return user

class AccountDetailsForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)