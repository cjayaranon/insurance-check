from django.urls import path
from . import views

urlpatterns = [
    path('pay-approver/', views.BMapprove.as_view(), name='pay-approver-link'),
]