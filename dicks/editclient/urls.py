from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

urlpatterns = [
    path('<pk>/edit-pending/', login_required(EditPendingPayments.as_view()), name = 'edit-pending'),
    path('<slug:pk>/', login_required(EditClientDetails.as_view()), name='edit-client'),
]