from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login,authenticate
# Create your views here.

def loginuser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        data=UserData.objects.filter(username=username)
        return render(request,'userpage.html',{'data':data})
    else:
        return render(request,'loginpage.html')

def register(request):
    if request.method=='POST':
        password=request.POST['password']
        repassword=request.POST['repassword']
        if password==repassword:

            name=request.POST['name']
            email=request.POST['email']
            username=request.POST['username']

            UserData.objects.create_user(name=name,email=email,username=username,password=password)
            return redirect(loginuser)
        else:
            return redirect(register)

        
    else:
        return render(request,'register.html')

def userpage(request):
    return render(request,'userpage.html')