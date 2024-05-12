from django import forms

from .  models import UserManagement,FacilityManagement,Appoint_Manage

class UsermanageForm(forms.ModelForm):
    class Meta:
        model = UserManagement
        fields = '__all__'
        widgets={
            'drname':forms.Select(attrs={'class':'form-control','placeholder':'select Doctor'}),
            'patientname':forms.Select(attrs={'class':'form-control','placeholder':'Enter the Patient name'}),
        }

class FacilityForm(forms.ModelForm):
    class Meta:
        model = FacilityManagement
        fields = '__all__'
        widgets={
            'location':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Location'}),
            'department':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Department'}),
            'resource':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Resource'}),

        }

class AppointmanageForm(forms.ModelForm):
    class Meta:
        model = Appoint_Manage
        fields = '__all__'
        widgets={
            'patientId':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the Patient Id'}),
            'doctorId':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the Doctor Id'}),
            'patientName':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Name'}),
            'dr_Name':forms.Select(attrs={'class':'form-control','placeholder':'select Doctor'}),
            'descrption':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Description'}),

        }


