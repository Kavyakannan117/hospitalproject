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
    doctors=Doctor.objects.all()
    patients=Patient.objects.all()
    if request.method == "POST":
        form=AppointmanageForm(request.POST,files=request.FILES)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('/success')
    else:
        form = AppointmanageForm()
    return render(request,'admin/add_appointment.html',{'form':form ,'patients':patients,'doctors':doctors})

def create_checkout_session(request):

    default_price_inr = 300 * 100  # Stripe expects the amount in cents

    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'INR',
                        'unit_amount': default_price_inr,
                        'product_data': {
                            'name': 'Product Name'  
                        },
                    },
                    'quantity': 1  
                }
            ],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('success')),
            cancel_url=request.build_absolute_uri(reverse('cancel'))
        )

        return redirect(checkout_session.url, code=303)


def success(request):
    appoint=Appointment.objects.all()
    appoint.delete()
    return render(request,'patient/success.html')

def cancel(request):

    return render(request,'patient/cancel.html')

def create_Patdetails(request):
    doctors=PatientManagement.objects.all()
    if request.method == "POST":
        form=PatientManageForm(request.POST,files=request.FILES)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('create-detailpat')
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

