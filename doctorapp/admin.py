from django.contrib import admin
from .models import Doctor,PatientManagement,AppointmentShedule,E_Prescription
# Register your models here.
admin.site.register(Doctor)
admin.site.register(PatientManagement)
admin.site.register(AppointmentShedule)
admin.site.register(E_Prescription)

