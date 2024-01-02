from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.core.mail import send_mail
from otpverifyproj import settings
import random


# Create your views here.

def login(request):
    return render(request,'login.html')

otp=random.randint(1111,9999)
def signup(request):
    if request.method=='POST':
        new=signupform(request.POST)
        if new.is_valid():
            new.save()
            print("Signup Successfully!")

            #Email Send for OTP
            global otp
            sub="Your One time password"
            msg=f"Hello User\n\nThanks for registration!\n\nYour One time password is {otp}\n\nPlease verify with this OTP, and enjoy services.\n\nThanks & Regards!\nTOPS Tech Team\n+91 9724799469 | www.tops-int.com"
            from_mail=settings.EMAIL_HOST_USER
            to_mail=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_mail,recipient_list=to_mail)
            return redirect('otpverify')
        else:
            print(new.errors)
    return render(request,'signup.html')

def home(request):
    return render(request,'home.html')

msg=""
def otpverify(request):
    global otp
    global msg
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            return redirect('login')
        else:
            msg="Invalid OTP...Please try again!"
            print(msg)
    return render(request,'otpverify.html',{'msg':msg})