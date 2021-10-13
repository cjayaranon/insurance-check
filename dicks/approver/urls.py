from django.urls import path
from . import views

urlpatterns = [
    path('pay-approver/', views.BMapprove.as_view(), name='pay-approver-link'),
    path('<pk>/update', views.ApproveView.as_view(), name='pay-approve-view'),
]