from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def index(request):
    if request.method=='POST':
        fnm=request.POST['firstname']
        lnm=request.POST['lastname']
        email=request.POST['email']
        dob=request.POST['dob']
        mob=request.POST['mobile']
        adr=request.POST['address']
        userinfo.objects.create(firstname=fnm,lastname=lnm,email=email,dob=dob,mobile=mob,address=adr)
        print("Record Inserted!")
    else:
        print("Error!")
    return render(request,'index.html')

def showdata(request):
    data=userinfo.objects.all()
    return render(request,'showdata.html',{'data':data})

def updatedata(request,id):
    stid=userinfo.objects.get(id=id)
    if request.method=='POST':
        fnm=request.POST['firstname']
        lnm=request.POST['lastname']
        email=request.POST['email']
        dob=request.POST['dob']
        mob=request.POST['mobile']
        adr=request.POST['address']
        userinfo.objects.filter(id=id).update(
            firstname=fnm,lastname=lnm,email=email,dob=dob,mobile=mob,address=adr
        )
        print("Record updated!")
        return redirect('showdata')
    else:
        print("Error!")
    return render(request,'updatedata.html',{'stid':stid})
    