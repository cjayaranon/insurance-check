from django.urls import path
from . import views

urlpatterns = [
    path('pay-approver/', views.BMapprove.as_view(), name='pay-approver-home'),
    path('<int:pay_details>/<int:pay_tag>/update', views.ApproveView.as_view(), name='pay-approve-view'),
]