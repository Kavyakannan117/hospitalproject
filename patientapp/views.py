from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect

from .models import Patient,Appointment,MedicalHistory,HealthEducation,Billing
from .forms import PatientForm,AppointmentForm,MedHistoryForm,HealthForm,BiilingForm

# Create your views here.
def index_view(request):
    if request.user.is_authenticated:
      return render(request,'patient/indexpat.html')


def RegisterPatient(request):
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
                return redirect('registerpatient')
            else:
                 patient=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,
                                           email=email,password=password)
            patient.save()
            return redirect('loginpatient')
        else:
            messages.info(request,'This password is not matching')
            return redirect('registerpatient')
    return render(request,'patient/registration_patient.html')

def LoginPatient(request):
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            patient=auth.authenticate(username=username,password=password)
            if patient is not None:
                auth.login(request,patient)
                return redirect('indexpat')
            else:
                messages.info(request,'Please provide correct details')
                return redirect('loginpatient')
        return render(request,'patient/login_patient.html')



def create_patient(request):
    patients=Patient.objects.all()
    if request.method == "POST":
        form=PatientForm(request.POST,files=request.FILES)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('/doctorlist')
    else:
        form = PatientForm()
    return render(request,'patient/create-patient.html',{'form':form ,'patients':patients})

def add_appiontment(request):
    appoint=Appointment.objects.all()
    if request.method == "POST":
        form=AppointmentForm(request.POST,files=request.FILES)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = AppointmentForm()
    return render(request,'patient/patientappoint.html',{'form':form ,'appoint':appoint})

def success(request):
    appoint=Appointment.objects.all()
    appoint.delete()
    return render(request,'patient/success.html')


def create_Patdetails(request):
    patient=MedicalHistory.objects.all()
    if request.method == "POST":
        form=MedHistoryForm(request.POST,files=request.FILES)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('listrecords')
    else:
        form = MedHistoryForm()
    return render(request,'patient/create-patdetails.html',{'form':form ,'patient':patient})

def listRecords(request):
    patient=MedicalHistory.objects.all()

    paginator=Paginator(patient,3)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'patient/listofrecords.html',{'patient':patient,'page':page})



def listBill(request):
    patient=Billing.objects.all()

    paginator=Paginator(patient,3)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'patient/bill_list.html',{'patient':patient,'page':page})


def create_Health(request):
    patient=HealthEducation.objects.all()
    if request.method == "POST":
        form=HealthForm(request.POST,files=request.FILES)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('listhealth')
    else:
        form = HealthForm()
    return render(request,'patient/create-health.html',{'form':form ,'patient':patient})

def listTips(request):
    patient=HealthEducation.objects.all()

    paginator=Paginator(patient,3)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'patient/healthlist.html',{'patient':patient,'page':page})

def logOut(request):
        auth.logout(request)
        return redirect('home')

