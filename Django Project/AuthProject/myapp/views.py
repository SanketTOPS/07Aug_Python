from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        fnm=signupdata.objects.get(username=unm)
        print("Firstname:",fnm.firstname)
        user=signupdata.objects.filter(username=unm,password=pas)
        if user: #true
            print("Login Successfully!")
            #request.session['user']=unm #session create
            request.session['user']=fnm.firstname
            return redirect('home')
        else:
            print("Error!Login faild....Try again")
    return render(request,'index.html')

def usersignup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
            return redirect('/')
        else:
            print(newuser.errors)
    return render(request,'usersignup.html')

def home(request):
    user=request.session.get('user')
    return render(request,'home.html',{'cuser':user})

def userlogout(request):
    logout(request)
    return redirect('/')

