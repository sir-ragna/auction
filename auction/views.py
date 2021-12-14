
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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
            return redirect('index')
    else:
        form = forms.UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required()
def create_listing(request):
    if request.method == 'POST':
        form = forms.ListingForm(request.POST)
        if form.is_valid():
            new_listing = form.save(commit=False)
            new_listing.seller = request.user
            new_listing.save()
            messages.info(request, "New action created")
            return redirect('index')
    else:
        form = forms.ListingForm()
    return render(request, 'create_listing.html.j2', {'form': form})