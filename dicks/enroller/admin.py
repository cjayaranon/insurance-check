from django.contrib import admin
from .models import Role, Client, Branch, Designation, Credits, Agent
# Register your admin here.



class RoleAdmin(admin.ModelAdmin):
    list_display = ['role_name', 'role_definitiion']
    
    
    
class ClientAdmin(admin.ModelAdmin):
    list_display = ['last_name','first_name','iaccs_id', 'role']
    
    
    
class BranchAdmin(admin.ModelAdmin):
    list_display = ['branch_name','address']
    
    
    
class DesignationAdmin(admin.ModelAdmin):
    list_display = ['designation_name','description']
    
    
    
class AgentAdmin(admin.ModelAdmin):
    list_display = ['last_name','first_name','id','branch','designation']
    
    
    
class CreditsAdmin(admin.ModelAdmin):
    list_display = ['amount','owner']
    
    
    
admin.site.register(Role, RoleAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Credits, CreditsAdmin)