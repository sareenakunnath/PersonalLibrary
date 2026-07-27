from  django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from  django.contrib.auth.forms import AuthenticationForm
from  django.contrib.auth import login,authenticate,logout

def signup(request):
    if request.method=="POST":
        form=CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form= CustomUserCreationForm()

    return render(request, "accounts/signup.html",{"form":form}) 

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            login(request,form.get_user())
            return redirect("book_list")
    else:
        form=AuthenticationForm()

    return render(request,"accounts/login.html",{"form":form})   

def logout_view(request):
    logout(request)
    return redirect("login")         







