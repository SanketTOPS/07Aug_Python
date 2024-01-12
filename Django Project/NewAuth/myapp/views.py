from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.


def index(request):
    msg=""
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            username=newuser.cleaned_data.get('username')
            try:
                usersignup.objects.get(username=username)
                print("Username is already exists!")
                msg="Username is already exists!"
            except usersignup.DoesNotExist:
                newuser.save()
                print("Signup Successfully!")
                msg="Signup Successfully!"
        else:
            print(newuser.errors)
            msg="Something went wrong...Try again!"
    return render(request,'user/index.html',{'msg':msg})


def userlogin(request):
    msg=""
    if request.method=='POST':
        r=request.POST['role']
        u=request.POST['username']
        p=request.POST['password']

        user=usersignup.objects.filter(role=r,username=u,password=p)
        c_id=usersignup.objects.get(username=u)
        print("Current ID:",c_id.id)
        c_role=c_id.role
        print("Current Role:",c_role)
        if user:
            print("Login Successfull!")
            msg="Login Successfull!"
            request.session['user']=u
            request.session['c_role']=c_role
            return redirect('home')
        else:
            print("Invalid Login Cred...!")
            msg="Invalid Username or Password...Try again!"
    return render(request,'user/userlogin.html',{'msg':msg})


def home(request):
    user=request.session.get('user')
    c_role=request.session.get('c_role')
    return render(request,'user/home.html',{'c_role':c_role,'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')