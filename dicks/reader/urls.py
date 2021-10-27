from django.contrib.auth.decorators import login_required
from django.urls import path
# from .forms import *
from .views import *


urlpatterns = [
    path('generate-report/viewing/', login_required(OwnBranchSalesResultsView.as_view()), name = 'reports-viewing'),
    path('generate-report/request/preview/', login_required(OwnBranchSalesFormPreview(ReportGenerateForm)), name='report-request-preview'),
    path('generate-report/', login_required(OwnBranchSales.as_view()), name = 'reports-home'),
    path('cancelled/', login_required(CancelledPayments.as_view()), name = 'reader-cancelled'),
    path('pending/', login_required(PendingPayments.as_view()), name = 'reader-pendings'),
    path('approved/', login_required(ApprovedPayments.as_view()), name = 'reader-approved'),
]