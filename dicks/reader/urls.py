from django.contrib.auth.decorators import login_required
from django.urls import path
# from .forms import *
from .views import *


urlpatterns = [
    path('pending/', login_required(PendingPayments.as_view()), name='reader-pendings'),
    path('approved/', login_required(ApprovedPayments.as_view()), name='reader-approved'),
]