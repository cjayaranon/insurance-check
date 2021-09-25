from django.contrib.auth.decorators import login_required
from django.urls import path
from .forms import *
from .views import *

urlpatterns = [
    path('home/', login_required(HomeView.as_view()), name='home'),
    path('search/<str:searchtext>/', SearchView.as_view(), name='search'),
    path('bio-encode/', login_required(BioEncodeView.as_view()), name='encode'),
    path('bio-encode/preview/', BioEncodeFormPreview(BioEncodeForm), name='encode-preview'),
    path('payment-encode/<int>', PaymentEncodeView.as_view(), name='pay-encode-details'),
    path('payment-encode/check/preview', PaymentDetailsFormPreview(PaymentDetailsForm), name='pay-preview'),
]