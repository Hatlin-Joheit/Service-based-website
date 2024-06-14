from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.

def jview(request):
    return render(request,'home.html')

def regview(request):
    return render(request,'reg.html')

def loginview(request):
    return render(request,'login.html')

def indexview(request):
    return render(request,'home.html')