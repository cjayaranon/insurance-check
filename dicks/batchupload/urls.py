from django.urls import path
from .forms import *
from . import views

urlpatterns = [
    path('excel-upload', views.ExcelUpload.as_view(), name='excel-up'),
    path('csv-upload', views.UploadCSV.as_view(), name='csv-up'),
]
