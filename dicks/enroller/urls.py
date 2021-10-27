from django.contrib.auth.decorators import login_required
from django.urls import path
from .forms import *
from .views import *

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='marketing-home'),
    path('search/<str:searchtext>/', login_required(SearchView.as_view()), name='search'),
    path('bio-encode/', login_required(BioEncodeView.as_view()), name='encode'),
    path('bio-encode/preview/', login_required(BioEncodeFormPreview(BioEncodeForm)), name='encode-preview'),
    path('payment-encode/<int>', login_required(PaymentEncodeView.as_view()), name='pay-encode-details'),
    path('payment-encode/check/preview', login_required(PaymentDetailsFormPreview(PaymentDetailsForm)), name='pay-preview'),
]