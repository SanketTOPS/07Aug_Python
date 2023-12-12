import random
from django.shortcuts import render,redirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest



# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method =="POST":
        try:
            user_data = User.objects.get( email=request.POST['email'])
            return render(request,'register.html',{'msg':'User already Exist'})
        except:
        
            if request.POST['pwd'] == request.POST['cpwd']:
                global fotp
                fotp = random.randint(1000,9999)
                subject = 'Your OTP Verfication'
                message = f"Hi your OTP is {fotp}, thank you for choosing us"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [ request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                global temp
                # User.objects.create(
                temp= {
                "name":request.POST["name"],
                "email":request.POST["email"],
                "password":request.POST["pwd"]
                }
                return render(request,'otp.html')
            
            else:
                return render(request,'register.html',{'msg':'password and confirm password not match'})
    else: 
        return render(request,'register.html')

def otp(request):
    if request.method=="POST":
        if fotp == int(request.POST['otp']):
            User.objects.create(
                name=temp["name"],
                email=temp["email"],
                password=make_password(temp["password"])
            )
            return render(request,'index.html')
        else:
            return render(request,'otp.html',{'msg':'OTP not match'})
    else :
        return render(request,'register.html')

def login(request):
    if request.method == "POST":
        try:
            user_data = User.objects.get(email=request.POST["email"])
            if check_password(request.POST["pwd"], user_data.password):
                request.session["email"] = request.POST["email"]
                session_data = User.objects.get(email=request.session["email"])
                return render(request, 'home.html', {"session_data": session_data})
            else:
                return render(request, 'login.html', {'msg': 'Password not match'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'msg': 'User not found. Please register.'})
    else:
        return render(request, 'login.html')