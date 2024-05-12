from django import forms
from .  models import Patient,Appointment,MedicalHistory,Billing,HealthEducation

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets={
            'patient_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Patient Name'}),
            'patient_age':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the Patient Age'}),
            'patient_address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Patient Address'}),
            'symptoms':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Patient Symptoms'}),

        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'
        widgets={
            'appointment':forms.DateField(),
            'doctorName':forms.Select(attrs={'class':'form-control','placeholder':'Select the Doctor name'}),

        }

class MedHistoryForm(forms.ModelForm):
    class Meta:
        model=MedicalHistory
        fields='__all__'
        widgets={
            'next_appoint':forms.DateField(),

        }

class BiilingForm(forms.ModelForm):
    class Meta:
        model=Billing
        fields='__all__'

class HealthForm(forms.ModelForm):
    class Meta:
        model=HealthEducation
        fields='__all__'




