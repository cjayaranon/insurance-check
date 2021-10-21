from django.contrib import admin
from .models import *
# Register your admin here.



class ClientAdmin(admin.ModelAdmin):
    list_display = ['membership_branch', 'id', 'last_name']
    
    
    
class PaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ['payor', 'date_of_payment', 'premium_paid', 'auth_agent']
    
    
    
class PayTagDetailsAdmin(admin.ModelAdmin):
    list_display = ['tag', 'payment', 'approver']

admin.site.register(Role)
admin.site.register(Client, ClientAdmin)
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
