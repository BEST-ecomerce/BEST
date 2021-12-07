from django.urls import path
from .views import HomeView, BreakfastView, LunchView, SupperView, DietView, LandingView
from . import views 

app_name = "main"

urlpatterns = [
    path('', LandingView.as_view(), name='index'),
    path('signup', views.signUp, name='signup'),
    path('login', views.loginPage, name='login'),
    path('home', HomeView.as_view(), name='home'),
    path('breakfast', BreakfastView.as_view(), name='breakfast'),
    path('lunch', LunchView.as_view(), name='lunch'),
    path('supper', SupperView.as_view(), name='supper'),
    path('diet', DietView.as_view(), name='diet'),
]
