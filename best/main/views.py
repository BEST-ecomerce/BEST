from django.contrib.auth.signals import user_logged_in
from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm
from .models import *

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

class LandingView(TemplateView):
    template_name = 'main/index.html'

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main:home')

    context = {}
    return render(request, 'main/login.html', context)

def signUp(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)


            return redirect('main:login')

    context = {'form':form}
    return render(request, 'main/signup.html', context)

class HomeView(TemplateView):
    template_name = 'main/home.html'

class LunchView(TemplateView):
    template_name = 'main/lunch.html'

class BreakfastView(TemplateView):
    template_name = 'main/breakfast.html'

class SupperView(TemplateView):
    template_name = 'main/supper.html'

class DietView(ListView):
    template_name = 'main/diets.html'
    model = DietProduct
    context_object_name = 'diet'