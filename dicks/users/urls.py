from django.urls import path
from . import views

urlpatterns = [
    path('/', views.LoginScreen.as_view(), name='login'),
]