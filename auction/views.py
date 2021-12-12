
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.contrib import messages
from django.contrib import auth
# Instead of importing 'authenticate' and 'login' from 'django.contrib.auth'
# I import 'auth' so I can use 'auth.authenticate()' and 'auth.login()' without
# having collisions with other functions called 'login' or 'authenticate'.

from . import forms

def index(request):
    return render(request, "index.html.j2")

def login(request):
    if request.method == 'POST':
        login_form = forms.UserLoginForm(request.POST)
        print("test1")
        if login_form.is_valid():
            print("test2")
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('index')
            else:
                messages.error(request, "Wrong username or password")
    else:    
        login_form = forms.UserLoginForm()
    return render(request, "login.html.j2", {'login_form': login_form})
