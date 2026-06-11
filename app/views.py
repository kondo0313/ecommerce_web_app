from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserSignupForm
from django.shortcuts import render, redirect

def index(request):
    return render(request, "app/test.html")

def admin_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "app/accounts/admin_register.html", {"form": form})

def user_register(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = UserSignupForm()
    return render(request, "app/accounts/user_register.html", {"form": form})