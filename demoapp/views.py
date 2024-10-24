from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from . models import Product

def demof(request):
    ob=Product.objects.all()   
    return render(request,'index.html',{'result':ob})
def addition(request):
    x=int(request.POST['num1'])
    y=int(request.POST['num2'])
    answer=x+y
    return render(request,'result.html',{'result':answer})
def addregister(request):
    return render(request,'register.html')
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['last_name']
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"The username is alreay exists")
                return redirect('demoapp:addregister')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"The Email is already exists")
                return redirect('demoapp:addregister')
            else:

                user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
                user.save()
                messages.info(request,"The User Created")
                return redirect('demoapp:demof')
        else:
            messages.info(request,"Retype your password again")
            return redirect('demoapp:addregister')
    return render(request,'register.html')
def addlogin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('demoapp:demof')
        else:
            messages.info(request,"Your credential is wrong")
            return redirect('demoapp:addlogin')

    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return render(request,'index.html')
def aboutf(request): 
    return render(request,'about.html')

        
        
        
        
