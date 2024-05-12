from django.contrib.auth.views import LoginView
from django.urls import path
from .import views

urlpatterns=[
    path('indexdoc/',views.index_view,name='indexdr'),

    path('registerdr/',views.RegisterDoctor,name='registerdr'),
    path('logindr/',views.LoginDoctor,name='logindr'),
    path('create-dr/',views.create_doctor,name='create-dr'),
    path('create-patientdetails/',views.create_patientdetails,name='patientdetails'),
    path('listappointdr/',views.listsofAppointment,name="listappointdr"),
    path('appointdr/',views.approvedr_appiontment,name='appointdr'),
    path('patientlist/',views.listPatient,name='patientlist'),

    path('detailspatient/<int:patient_id>/',views.detailspatient,name="patientdetails"),
    path('updatepatient/<int:patient_id>/',views.updatepatient,name="patientupdate"),
    path('deletepatient/<int:patient_id>/',views.deletepatient,name="patientdelete"),

    path('listschedule/',views.listSchedule,name="listschedule"),
    path('deleteschedule/<int:appoint_id>/',views.deleteschedule,name="deleteschedule"),

    path('create-prescrption/',views.create_prescrption,name='create-prescrption'),
    path('detailsprescrption/',views.listPrescrptions,name="patientprescrption"),

    path('updateprescption/<int:patient_id>/',views.updateprescrption,name="updateprescption"),
    path('deleteprescption/<int:patient_id>/',views.deleteprescrption,name="deleteprescption"),

]
