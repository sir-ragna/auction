
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html.j2")

def login(request):
    return render(request, "login.html.j2")