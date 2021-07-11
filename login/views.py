from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def LoginPage(request):
    context = {}
    return render(request, 'login/login.html')
        