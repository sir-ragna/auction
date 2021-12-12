
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

def register(request):
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.save()
            return HttpResponseRedirect("/")
    else:
        form = forms.UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

