from django.shortcuts import render
from django.http import HttpResponse
import os

def hello(request):
   return render(request,'hello.html', {})

# Create your views here.
