from django import forms
from django.contrib.auth.models import User
from appBlog.models import *



class Publication_form(forms.Form):
    
    title = forms.CharField(max_length=60) #Titulo
    caption = forms.CharField(max_length=60) #Subtitulo
    sub_category = forms.CharField(max_length=20) #Subcategoria
    author = forms.CharField(max_length=60) #Autor models.ForeignKey(User, on_delete=models.CASCADE) <- ¡Si borramos al autor va a borrar por cascada los posteos realizados por el mismo!
    body = forms.CharField(max_length=9600) #Cuerpo
    publication_date = forms.DateTimeField() #Fecha de publicacion

    class Meta:
        model = Publication
        fields = ('title', 'caption', 'sub_category', 'author', 'body', 'publication_date')

         






"""
    class ProfeForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=50)



    class Literatura_Form(forms.Form):
    nombre_literatura = forms.CharField(max_length=50)
    autor_literatura = forms.CharField(max_length=50)
    editorial_literatura = forms.CharField(max_length=50)
    descripcion_literatura = forms.CharField(widget=CKEditorWidget())
    imglit = forms.ImageField(required=False)
"""