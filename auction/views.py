
from django.http import HttpResponse
from django.shortcuts import render

from . import forms

def index(request):
    return render(request, "index.html.j2")

def login(request):
    login_form = forms.UserLoginForm()
    return render(request, "login.html.j2", {'login_form': login_form})
