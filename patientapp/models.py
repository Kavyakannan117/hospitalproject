from django.db import models

from doctorapp.models import Doctor,PatientManagement


# Create your models here.

class Patient(models.Model):
    patient_name=models.CharField(max_length=200)
    patient_age=models.IntegerField()
    patient_address=models.CharField(max_length=200)
    symptoms=models.CharField(max_length=200)
    assignedDoctorId=models.PositiveIntegerField(null=True)


class Appointment(models.Model):
    appiontment=models.DateField(auto_now=True)
    description=models.CharField(max_length=1000)
    patientName=models.CharField(max_length=300)
    doctorName=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    def __str__(self):
         return '{}'.format(self.appiontment)

class MedicalHistory(models.Model):
    name=models.CharField(max_length=200)
    medical_record=models.CharField(max_length=1500)
    treatment=models.CharField(max_length=2500)
    medicine=models.CharField(max_length=250)
    next_visit=models.DateField()

    def __str__(self):
         return '{}'.format(self.next_visit)

class Billing(models.Model):
    medicine_cost=models.PositiveIntegerField(null=False)
    drFee=models.PositiveIntegerField(null=False)
    total_amount=models.PositiveIntegerField(null=False)
    insurance_num=models.IntegerField()

    def __str__(self):
         return '{}'.format(self.total_amount)

class HealthEducation(models.Model):
    tips=models.CharField(max_length=250)
    resource=models.CharField(max_length=200)

    def __str__(self):
         return '{}'.format(self.resource)
