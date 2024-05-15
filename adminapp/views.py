import stripe
from django.conf import settings
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q

from doctorapp.forms import DoctorForm
from doctorapp.models import Doctor
from patientapp.forms import BiilingForm
from patientapp.models import Patient, Billing
from .models import UserManagement,Appoint_Manage,FacilityManagement
from . forms import UsermanageForm,AppointmanageForm,FacilityForm
from django.shortcuts import render, redirect


# Create your views here.
def home_view(request):
    return render(request,'admin/home.html')

def index_view(request):
    if request.user.is_authenticated:
      return render(request,'admin/index.html')

def RegisterUser(request):
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
                return redirect('register')
            else:
                 user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,
                                           email=email,password=password)
            user.save()
            return redirect('login')
        else:
            messages.info(request,'This password is not matching')
            return redirect('register')
    return render(request,'admin/registration.html')

def LoginUser(request):
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('index')
            else:
                messages.info(request,'Please provide correct details')
                return redirect('login')
        return render(request,'admin/login.html')


def approve_appiontment(request):
    doctors=Doctor.objects.all()
    patients=Patient.objects.all()
    if request.method == "POST":
        form=AppointmanageForm(request.POST,files=request.FILES)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('/doctorlist')
    else:
        form = AppointmanageForm()
    return render(request,'admin/add_appointment.html',{'form':form ,'patients':patients,'doctors':doctors})

def listDoctor(request):
    doctors=Doctor.objects.all()

    paginator=Paginator(doctors,3)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'admin/listdoctor.html',{'doctors':doctors,'page':page})


def SearchDoctor(request):
    query=None
    doctors=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        doctors=Doctor.objects.filter(Q(department__icontains=query)|Q(name__contains=query))
    else:
        doctors=[]
    context={'doctors':doctors,'query':query}

    return render(request,'admin/search.html', context)

def detailsDoctor(request,doctor_id):
    doctor=Doctor.objects.get(id=doctor_id)
    return render(request,'admin/detailsview.html',{'doctor':doctor})

def updateDoctor(request,doctor_id):
    doctor=Doctor.objects.get(id=doctor_id)
    if request.method=='POST':
        form=DoctorForm(request.POST ,request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('/doctorlist')
    else:
        form=DoctorForm(instance=doctor)
    return render(request,'admin/updateview.html',{'form':form})

def deleteDoctor(request,doctor_id):
    doctor=Doctor.objects.get(id=doctor_id)
    if request.method == "POST":
        doctor.delete()
        return redirect('/doctorlist')
    return render(request,'admin/deleteview.html',{'doctor':doctor})

def listAppointment(request):
    appoints=Appoint_Manage.objects.all()

    paginator=Paginator(appoints,3)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'admin/list-appoint.html',{'appoints':appoints,'page':page})


def confirm_appointment(request,appoint_id):
    appoint=Appoint_Manage.objects.get(id=appoint_id)
    if request.method=='POST':
            appoint.save()
            return redirect('/listconfirmappoints')
    return render(request,'admin/confirm-appoint.html',{'appoint':appoint})


def delete_appointment(request,appoint_id):
    appoint=Appoint_Manage.objects.get(id=appoint_id)
    if request.method == "POST":
        appoint.delete()
        return redirect('/listappoint')
    return render(request,'admin/delete-appoint.html',{'appoint':appoint})

def list_appointment_approved(request):
    appoints=Appoint_Manage.objects.all()

    paginator=Paginator(appoints,3)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'admin/list-confirm-appoint.html',{'appoints':appoints,'page':page})


def create_facility(request):
    details=FacilityManagement.objects.all()
    if request.method == "POST":
        form=FacilityForm(request.POST,files=request.FILES)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('/facilitylist')
    else:
        form = FacilityForm()
    return render(request,'admin/create-facility.html',{'form':form ,'details':details})

def list_facility(request):
    details=FacilityManagement.objects.all()

    paginator=Paginator(details,3)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'admin/list-facility.html',{'details':details,'page':page})

def create_Bill(request):
    patient=Billing.objects.all()
    if request.method == "POST":
        form=BiilingForm(request.POST,files=request.FILES)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('listbill')
    else:
        form = BiilingForm()
    return render(request,'admin/create-bill.html',{'form':form ,'patient':patient})

def logout(request):
        auth.logout(request)
        return redirect('home')



