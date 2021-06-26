from django.shortcuts import render,redirect
from django.conf import settings
from .models import Student
from django.contrib import messages
from django.http import HttpResponse


def index(request):
    if request.method=='POST':
        id=request.POST.get('id','')
        usn=request.POST.get('usn','')
        name=request.POST.get('name','')
        sem=request.POST.get('sem','')
        phone=request.POST.get('phone','')
        email=request.POST.get('email','')
        if id and usn and name and sem and phone and email:
            form=Student(id=id,usn=usn,name=name,sem=sem,phone=phone,email=email)
            form.save()
            messages.success(request, "form submitted successfully")
        else:
            return HttpResponse("enter all the details")
    return render(request,"index.html")
