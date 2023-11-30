from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=signupdata.objects.filter(username=unm,password=pas)
        if user: #true
            print("Login Successfully!")
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
    return render(request,'home.html')