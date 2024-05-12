from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=500)
    descrption=models.CharField(max_length=500)
    education=models.CharField(max_length=200)
    mobile=models.CharField(max_length=100)
    department=models.CharField(max_length=200)
    dr_id=models.IntegerField()
    def __str__(self):

        return '{}'.format(self.name)


class PatientManagement(models.Model):
    patient_records=models.CharField(max_length=200)
    medical_history=models.CharField(max_length=100)
    treatment_plans=models.CharField(max_length=500)
    decision_making=models.CharField(max_length=200)

class AppointmentShedule(models.Model):
    schedule=models.DateField(auto_now=False)
    appointment_details=models.CharField(max_length=100)
    patient_info=models.CharField(max_length=200)

class E_Prescription(models.Model):
    patient_name=models.CharField(max_length=200)
    prescription=models.CharField(max_length=1500)
    dosage=models.CharField(max_length=500)
    pharmacies=models.CharField(max_length=400)
