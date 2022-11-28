from django.shortcuts import render
from django.http import  HttpResponse
from django.shortcuts import render
from django import template

def home(request):
    return render(request, 'templates/index.html')

# Create your views here.
