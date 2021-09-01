from django.urls import path
from .forms import *
# from enroller.preview import *
from . import views

urlpatterns = [
    path('search/<pk>/', views.SearchView.as_view(), name='search'),
    path('bio-encode/', views.BioEncodeView.as_view(), name='encode'),
    path('payment-details/', views.PaymentEncodeView.as_view(), name='pay-details'),
    path('post/', views.BioEncodeFormPreview(BioEncodeForm), name='post')
]