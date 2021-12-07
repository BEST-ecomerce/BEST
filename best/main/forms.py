import django
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField

class CreateUserForm(UserCreationForm):
    username = forms.CharField(label="username", max_length=150, min_length=5, widget=forms.TextInput(
        attrs={
            'class': 'border border-gray-300 py-2 px-4 rounded-md outline-white focus:border-green-400',
            'placeholder': 'Your user Name'
        }
    ))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(
        attrs={
            'class': 'border border-gray-300 py-2 px-4 rounded-md outline-white focus:border-green-400',
            'placeholder': 'Your email address'
        }
    ))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={
            'class': 'border border-gray-300 py-2 px-4 rounded-md outline-white focus:border-green-400',
            'placeholder': 'Your Password'
        }
    ))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={
            'class': 'border border-gray-300 py-2 px-4 rounded-md outline-white focus:border-green-400',
            'placeholder': 'Confirm you password'
        }
    ))

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError('Email Already Exist')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError('Password Do not Match')
        return password2
    
    def save(self, commit = True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user