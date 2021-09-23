from django.urls import path
from . import views

urlpatterns = [
    path('<slug:pk>/', views.EditClientDetails.as_view(), name='edit-client'),
]