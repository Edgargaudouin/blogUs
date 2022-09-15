from django.shortcuts import render
from appBlog.models import *
from appBlog.forms import *
# Create your views here.

def home(request):
    return render(request, 'appblog/home.html')


def add_publication(request):
    if request.method =='POST':
        form = Publication_form(request.POST)     #CREAR   
        
        if form.is_valid():
            data = form.cleaned_data
            title = data['title']
            caption = data['caption']
            sub_category = data['sub_category']
            author = data['author']
            body = data['body']
            publication_date = data['publication_date']
            publi = Publication(title=title, caption=caption, sub_category=sub_category, author=author, body=body, publication_date=publication_date) 
            publi.save()
            return render (request, 'appblog/home.html', {'message': "Publicacion creada"})
        else: 
            return render (request, 'appblog/home.html', {'message':"Error"})
    else:
        form = Publication_form()   #Medoto GET envia el formulario vacio
        return render (request, 'appblog/publication/publicationForm.html', {'formulary' : form})


def see_publication(request):
    publication = Publication.objects.all()
    return render(request, 'appblog/publication/publications.html', {'publication' : publication })


