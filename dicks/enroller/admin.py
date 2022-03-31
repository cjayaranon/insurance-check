from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin
# Register your admin here.



class ExportClient(ImportExportMixin, admin.ModelAdmin):
    list_display = ['membership_branch', 'id', 'last_name', 'first_name']
    search_fields = ['id', 'last_name', 'first_name']



class ClientAdmin(admin.ModelAdmin):
    list_display = ['membership_branch', 'id', 'last_name']
    
    
    
class PaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ['payor', 'id', 'date_of_payment', 'premium_paid', 'auth_agent', 'encoder_branch']
    
    
    
class PayTagDetailsAdmin(admin.ModelAdmin):
    list_display = ['tag', 'payment', 'approver']

admin.site.register(Role)
# admin.site.register(Client, ClientAdmin)
admin.site.register(Client, ExportClient)
admin.site.register(Branch)
admin.site.register(Designation)
admin.site.register(Agent)
admin.site.register(Credits)
admin.site.register(PaymentDetails, PaymentDetailsAdmin)
admin.site.register(PaymentType)
admin.site.register(ClientTagging)
admin.site.register(CutoffPeriod)
admin.site.register(PremiumAmount)
admin.site.register(PaymentTagging, PayTagDetailsAdmin)
