from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib.auth import authenticate

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from movies.forms import LoginForm
from .models import User
from .decorators import unauthonticated_user, allowed_users

# @unauthonticated_user
def LoginPage(request): 
    if request.method == "POST":
        form = LoginForm(request.POST)
        email = form.data['email']
        password = form.data['password']
        auth = authenticate(email=email, password=password)
        request.session['email'] = form.data['email']
        if auth:
            messages.success(request, f'Details for {email} Login Successfully.')
            return redirect('home')
        else:
            messages.warning(request, f'Error')
    else:
        form = LoginForm()

    return render(request,'login/login.html',{"form":form})



def LogOut(request) :	
	return render(request,'login/login.html',{"form":LoginForm()})