from django.shortcuts import render
from appBlog.models import *
# Create your views here.

def home(request):
    return render(request, 'appblog/home.html')

def see_publication(request):
    publication = Publication.objects.all()
    return render(request, 'appblog/publication/publications.html', {'publication' : publication })


