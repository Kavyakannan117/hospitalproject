from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.forms import models
from django.shortcuts import render, redirect

from adminapp.models import Appoint_Manage
from .models import Doctor,PatientManagement,AppointmentShedule,E_Prescription
from .forms import DoctorForm,PatientManageForm,AppointmentScheduleForm,E_PrescriptionForm
# Create your views here.
def index_view(request):
    if request.user.is_authenticated:
      return render(request,'doctor/indexdr.html')

def RegisterDoctor(request):
    if request.method=='POST':
        username=request.POST.get('username')
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('password1')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This user already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('registerdr')
            else:
                 doctor=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,
                                           email=email,password=password)
            doctor.save()
            return redirect('logindr')
        else:
            messages.info(request,'This password is not matching')
            return redirect('registerdr')
    return render(request,'doctor/registration_dr.html')

def LoginDoctor(request):
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            doctor=auth.authenticate(username=username,password=password)
            if doctor is not None:
                auth.login(request,doctor)
                return redirect('indexdr')
            else:
                messages.info(request,'Please provide correct details')
                return redirect('logindr')
        return render(request,'doctor/login_dr.html')


def create_doctor(request):
    doctors=Doctor.objects.all()
    if request.method == "POST":
        form=DoctorForm(request.POST,files=request.FILES)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('/doctorlist')
    else:
        form = DoctorForm()
    return render(request,'doctor/create-dr.html',{'form':form ,'doctors':doctors})

def create_patientdetails(request):
    doctors=PatientManagement.objects.all()
    if request.method == "POST":
        form=PatientManageForm(request.POST,files=request.FILES)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('patientlist')
    else:
        form = PatientManageForm()
    return render(request,'doctor/create-patientdetails.html',{'form':form ,'doctors':doctors})

def listPatient(request):
    doctors=PatientManagement.objects.all()

    paginator=Paginator(doctors,3)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'doctor/listpatients.html',{'doctors':doctors,'page':page})


def listsofAppointment(request):
    appoints=Appoint_Manage.objects.all()

    paginator=Paginator(appoints,3)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'doctor/list-appointdr.html',{'appoints':appoints,'page':page})

def detailspatient(request,patient_id):
    patient=PatientManagement.objects.get(id=patient_id)
    return render(request,'doctor/patientdetails.html',{'patient':patient})

def updatepatient(request,patient_id):
    patient=PatientManagement.objects.get(id=patient_id)
    if request.method=='POST':
        form=PatientManageForm(request.POST ,request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patientlist')
    else:
        form=PatientManageForm(instance=patient)
    return render(request,'doctor/patientupdate.html',{'form':form})

def deletepatient(request,patient_id):
    patient=PatientManagement.objects.get(id=patient_id)
    if request.method == "POST":
        patient.delete()
        return redirect('patientlist')
    return render(request,'doctor/patientdelete.html',{'patient':patient})

def approvedr_appiontment(request):
    appoint=AppointmentShedule.objects.all()
    if request.method == "POST":
        form=AppointmentScheduleForm(request.POST,files=request.FILES)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('/listconfirmappoints')
    else:
        form = AppointmentScheduleForm()
    return render(request,'doctor/schedule_appointment.html',{'form':form ,'appoint':appoint})

def listSchedule(request):
    appoints=AppointmentShedule.objects.all()

    paginator=Paginator(appoints,3)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'doctor/list-appointSchedule.html',{'appoints':appoints,'page':page})

def deleteschedule(request,appoint_id):
    appoints=AppointmentShedule.objects.get(id=appoint_id)
    if request.method == "POST":
        appoints.delete()
        return redirect('listschedule')
    return render(request,'doctor/deleteschedule.html',{'appoints':appoints})



def create_prescrption(request):
    patient=AppointmentShedule.objects.all()
    if request.method == "POST":
        form=E_PrescriptionForm(request.POST,files=request.FILES)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('patientprescrption')
    else:
        form = E_PrescriptionForm()
    return render(request,'doctor/create-prescrption.html',{'form':form ,'patient':patient})


def listPrescrptions(request):
    patient=E_Prescription.objects.all()

    paginator=Paginator(patient,3)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'doctor/medicinedetails.html',{'patient':patient,'page':page})

def updateprescrption(request,patient_id):
    patient=E_Prescription.objects.get(id=patient_id)
    if request.method=='POST':
        form=E_PrescriptionForm(request.POST ,request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patientlist')
    else:
        form=E_PrescriptionForm(instance=patient)
    return render(request,'doctor/updateprescrption.html',{'form':form})

def deleteprescrption(request,patient_id):
    patient=E_Prescription.objects.get(id=patient_id)
    if request.method == "POST":
        patient.delete()
        return redirect('patientlist')
    return render(request,'doctor/deleteprescrption.html',{'patient':patient})
