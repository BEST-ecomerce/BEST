from django.urls import path
from .views import HomeView, BreakfastView, LunchView, SupperView, DietView, LandingView, SignUpView, LoginView

app_name = "main"

urlpatterns = [
    path('', LandingView.as_view(), name='index'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('home', HomeView.as_view(), name='home'),
    path('breakfast', BreakfastView.as_view(), name='breakfast'),
    path('lunch', LunchView.as_view(), name='lunch'),
    path('supper', SupperView.as_view(), name='supper'),
    path('diet', DietView.as_view(), name='diet'),
]
