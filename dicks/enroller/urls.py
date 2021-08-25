from django.urls import path

from . import views

urlpatterns = [
    path('search/<pk>/', views.SearchView.as_view(), name='search'),
    path('encode/', views.EncodeView.as_view(), name='encode'),
]