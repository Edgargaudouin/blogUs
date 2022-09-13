from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Publication(models.Model):
    id = models.AutoField(primary_key=True) #ID publicación
    title = models.CharField(max_length=60) #Titulo
    caption = models.CharField(max_length=60) #Subtitulo
    category = models.CharField(max_length=20) #Categoria
    sub_category = models.CharField(max_length=20) #Subcategoria
    author = models.CharField(max_length=25) #Autor
    body = models.TextField(max_length=9600) #Cuerpo
    publication_date = models.DateTimeField() #Fecha de publicacion


    def __str__(self):
        return f"Blog: {self.title} - {self.author} - {self.publication_date}"

#Falta crear la imagen de la clase Publish

class User(models.Model):
    id = models.AutoField(primary_key=True) #ID cliente
    name = models.CharField(max_length=20) #Nombre
    lastname = models.CharField(max_length=20) #Apellido
    nickname = models.CharField(max_length=20, unique=True) #Apodo
    password = models.CharField(max_length=35) #Contraseña
    email = models.EmailField(unique=True) #Email
    birth_date = models.DateField() #Fecha de nacimiento
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True) #Hay que conectar con avatares

    def __str__(self):
        return f"Usuario: {self.name} {self.lastname} - {self.nickname}"

class Comment(models.Model):
    commenter_id = models.CharField(max_length=300) #ID comentarista #Debe pegar con el ID usuario investigar foreign key / clave foranea
    commenter_name = models.CharField(max_length=200) #Nombre comentarista
    comment_body = models.TextField(max_length=300) #Cuerpo de comentario
