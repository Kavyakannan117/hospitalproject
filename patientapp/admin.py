from django.contrib import admin
from .models import Patient,Appointment,MedicalHistory,Billing,HealthEducation

# Register your models here.

admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(MedicalHistory)
admin.site.register(Billing)
admin.site.register(HealthEducation)

