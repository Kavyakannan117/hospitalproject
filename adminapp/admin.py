from django.contrib import admin
from .models import UserManagement,FacilityManagement,Appoint_Manage
# Register your models here.
admin.site.register(UserManagement)
admin.site.register(FacilityManagement)
admin.site.register(Appoint_Manage)
