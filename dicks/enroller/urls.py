from django.urls import path
from .forms import *
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('search/<str:searchtext>/', views.SearchView.as_view(), name='search'),
    path('bio-encode/', views.BioEncodeView.as_view(), name='encode'),
    path('bio-encode/preview/', views.BioEncodeFormPreview(BioEncodeForm), name='encode-preview'),
    path('payment-encode/<int>', views.PaymentEncodeView.as_view(), name='pay-encode-details'),
    path('payment-encode/check/preview', views.PaymentDetailsFormPreview(PaymentDetailsForm), name='pay-preview'),
]