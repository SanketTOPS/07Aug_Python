from django.shortcuts import render
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
    