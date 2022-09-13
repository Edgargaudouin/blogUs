from django.shortcuts import render
from appBlog.models import *
# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def publication(request):
    return render(request, 'publication/publications.html')

def user(request):
    return render(request, 'user/users.html')

