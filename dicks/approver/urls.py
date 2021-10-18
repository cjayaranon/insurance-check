from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('', login_required(views.BMapprove.as_view()), name='pay-approver-home'),
    path('<int:pay_details>/<int:pay_tag>/update', login_required(views.ApproveView.as_view()), name='pay-approve-view'),
]