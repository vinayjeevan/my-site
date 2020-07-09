from django.contrib import admin
from app_site.models import Company_name, Agent_name

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=['com_name','com_location']
admin.site.register(Company_name,CompanyAdmin)   

class AgentAdmin(admin.ModelAdmin):
    list_display=['emp_name','call_atd','time_dur']
admin.site.register(Agent_name,AgentAdmin)