from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login,logout,authenticate
from .forms import InsertForm,DoctorForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

# Create your views here.

def index(r):
    data = {
        "doctors":Doctor.objects.all(),
        "patients" :Patient.objects.all()
    }
    return render(r,"home.html",data)

def appoiment(r):
    form = UserCreationForm(r.POST or None)

    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("signin")
    return render(r,"appoiment.html",{"form":form})

def insertDoctor(r):
    form = DoctorForm(r.POST or None)
    
    if r.method == "POST":
        if form.is_valid():
           form.save()
           return redirect(InsertForm)

def signin(r):
    form = AuthenticationForm(r.POST or None)

    if r.method == "POST":
        username = r.POST.get("username")
        password = r.POST.get("password")

        user  = authenticate(username=username,password=password)

        if user is not None:
            login(r,user)
            back = r.GET.get("next","/")
            return redirect(back)
            
        
    return render(r,"login.html",{"form":form})

def logout(r):
    return render(r,"logout.html")


