from django.contrib import admin
from .models import *
# Register your admin here.



class ClientAdmin(admin.ModelAdmin):
    list_display = ['membership_branch', 'last_name']

admin.site.register(Role)
admin.site.register(Client, ClientAdmin)
admin.site.register(Branch)
admin.site.register(Designation)
admin.site.register(Agent)
admin.site.register(Credits)
admin.site.register(PaymentDetails)
admin.site.register(PaymentType)
admin.site.register(ClientTagging)
admin.site.register(CutoffPeriod)
admin.site.register(PremiumAmount)
