from django.shortcuts import render,redirect
from .forms import * 
from .models import *

# Create your views here.

def index(request):
    if request.method=='POST':
        data=userForm(request.POST)
        if data.is_valid(): #true
            data.save()
            print("Your data has been saved!")
        else:
            print(data.errors)
    return render(request,'index.html')

def showdata(request):
    data=userInfo.objects.all()
    return render(request,'showdata.html',{'data':data})

def updatedata(request,id):
    stid=userInfo.objects.get(id=id)
    if request.method=='POST':
        data=userForm(request.POST,instance=stid)
        if data.is_valid(): #true
            data.save()
            print("Your data has been updated!")
            return redirect('showdata')
        else:
            print(data.errors)
    return render(request,'updatedata.html',{'stid':stid})

def deletedata(request,id):
    stid=userInfo.objects.get(id=id)
    userInfo.delete(stid)
    return redirect('showdata')
