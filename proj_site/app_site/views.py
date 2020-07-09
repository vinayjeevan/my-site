from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app_site.models import Agent_name

# Create your views here.
# def home(request):
#     return render(request,'home.html')

def user_login(request):
    print("=====================>")
    if request.method == 'POST':
        #if user exists, with username and password
        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            print("=====>")
            return redirect(Agent_details)
            #return render(request,'dashboard.html')
        else:
            return render(request,'home.html',{'error':"userdetails not exists"})    
    else:
        return render(request,'home.html')     

def signup(request):
    if request.method == 'POST':
       # to create a user
        if request.POST['password1'] == request.POST['password2']: # both password matched
            try:
               user = User.objects.get(username=request.POST['username'])
               return render(request, 'register.html',{'error': "username name already exists"})
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['username'],password=request.POST['password1'])
                return redirect(user_login)
        else:
            return render(request, 'register.html',{'error': "Password did't matched"})
    else:   
       return render(request,'register.html')    



def Agent_details(request):
    obj=Agent_name.objects.all()
    print("obj========>",obj)
    return render(request,'dashboard.html',{'obj':obj})