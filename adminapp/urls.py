from django.urls import path
from .import views

urlpatterns=[
    path('',views.home_view,name='home'),
    path('index/',views.index_view,name='index'),



    path('register/',views.RegisterUser,name='register'),
    path('login/',views.LoginUser,name='login'),
    path('appoint/',views.approve_appiontment,name='appoint'),

    path('doctorlist/',views.listDoctor,name='doctorlist'),
    path('search/',views.SearchDoctor,name='search'),

    path('detailsview/<int:doctor_id>/',views.detailsDoctor,name="details"),
    path('updateview/<int:doctor_id>/',views.updateDoctor,name="update"),
    path('deleteview/<int:doctor_id>/',views.deleteDoctor,name="delete"),

    path('listappoint/',views.listAppointment,name="listappoint"),
    path('listconfirmappoints/',views.list_appointment_approved,name="listconfirmappoints"),
    path('approve/<int:appoint_id>/',views.confirm_appointment,name="approve"),
    path('deleteappoint/<int:appoint_id>/',views.delete_appointment,name="delete-appoint"),

    path('createfacility/',views.create_facility,name="create-facility"),
    path('facilitylist/',views.list_facility,name="facilitylist"),

    path('createbill/',views.create_Bill,name="createbill"),
    path('logout/',views.logout,name='logout'),


]
