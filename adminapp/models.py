from django.db import models

from doctorapp.models import Doctor
from patientapp.models import Patient


# Create your models here.
class UserManagement(models.Model):
    drname=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patientname=models.ForeignKey(Patient,on_delete=models.CASCADE)


class FacilityManagement(models.Model):
    location=models.CharField(max_length=500)
    department=models.CharField(max_length=500)
    resource=models.CharField(max_length=400)

class Appoint_Manage(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=50,null=True)
    drName=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appointmentDate=models.DateField(auto_now=False)
    descrption=models.CharField(max_length=500)
