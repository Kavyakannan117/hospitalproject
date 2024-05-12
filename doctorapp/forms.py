from django import forms
from . models import Doctor,PatientManagement,AppointmentShedule,E_Prescription

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Doctor Name'}),
            'dr_id':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Id Number'}),
            'descrption':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Description'}),
            'education':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Qualification'}),
            'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Number'}),
            'department':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Department'}),
        }



class PatientManageForm(forms.ModelForm):
    class Meta:
        model=PatientManagement
        fields='__all__'
        widgets={
             'patient_records':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Patient Records'}),
             'medical_history':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the History'}),
             'treatment_plans':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Treatment Methods'}),
             'decision_making':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Decision'}),
        }

class AppointmentScheduleForm(forms.ModelForm):
    class Meta:
        model=AppointmentShedule
        fields='__all__'



class E_PrescriptionForm(forms.ModelForm):
    class Meta:
        model=E_Prescription
        fields='__all__'
        widgets={
             'patient_namew':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Treatment Methods'}),
             'prescription':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Treatment Methods'}),
             'dosage':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Decision'}),
        }
