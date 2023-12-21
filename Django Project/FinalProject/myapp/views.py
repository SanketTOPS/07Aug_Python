from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import logout

status=False
def index(request):
    global status
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Signup Successfully!")
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':

            unm=request.POST['username']
            pas=request.POST['password']

            user=signupmaster.objects.filter(username=unm,password=pas)
            uid=signupmaster.objects.get(username=unm)
            print("UserID:",uid.id)
            if user:
                print("Login Successfully!")
                request.session['user']=unm
                request.session['uid']=uid.id
                #msg="Login Successfully!"
                status=True
                return redirect('notes')
            else:
                print("Error!Login Fail...Try again")
    return render(request,'index.html')

def notes(request):
    #global status
    user=request.session.get('user')
    return render(request,'notes.html',{'user':user})

def profile(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    cuser=signupmaster.objects.get(id=uid)
    if request.method=='POST':
        newuser=updateForm(request.POST,instance=cuser)
        if newuser.is_valid():
            newuser.save()
            print("Profile updated!")
            return redirect("notes")
        else:
            print(newuser.errors)
    return render(request,'profile.html',{'user':user,'cuser':cuser})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def userlogout(request):
    logout(request)
    return redirect('/')