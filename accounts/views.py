from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from .forms import LoginForm

def login_check(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        name = request.POST["username"]
        pwd = request.POST["password"]
        user = authenticate(request, username=name, password=pwd)     
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'accounts/login.html')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {"form":form})

def logout(request):
    django_logout(request)
    return redirect("/")
