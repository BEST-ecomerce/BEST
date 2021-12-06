from django.views.generic import TemplateView, ListView
from .models import *

class LandingView(TemplateView):
    template_name = 'main/index.html'

class LoginView(TemplateView):
    template_name = 'main/login.html'

class SignUpView(TemplateView):
    template_name = 'main/signup.html'

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