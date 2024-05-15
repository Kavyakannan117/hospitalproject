from django.contrib.auth.views import LoginView
from django.urls import path
from .import views

urlpatterns=[
    path('indexpatient/',views.index_view,name='indexpat'),

    path('registerpatient/',views.RegisterPatient,name='registerpatient'),
    path('loginpatient/',views.LoginPatient,name='loginpatient'),
    path('create-patient/',views.create_patient,name='create-patient'),
    path('appointpatient/',views.add_appiontment,name='appointpatient'),
    path('success/',views.success,name='success'),
    path('patdetails',views.create_Patdetails,name='create-detailpat'),

    path('patientlist/',views.listPatient,name='patientlist'),

    path('healthcreate',views.create_Health,name='healthcreate'),

    path('listhealth/',views.listTips,name="listhealth"),
    path('listbill/',views.listBill,name="listbill"),
    
    path('logoutpatient/',views.logOut,name='logoutpat'),

    path('create-checkout-session/',views.create_checkout_session,name='create-checkout-session'),
    path('cancel/',views.cancel,name='cancel'),


]
