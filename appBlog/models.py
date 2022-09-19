from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.

class Publication(models.Model):
    id = models.AutoField(primary_key=True) #ID publicación
    title = models.CharField(max_length=60) #Titulo
    caption = models.CharField(max_length=60) #Subtitulo
    sub_category = models.CharField(max_length=20) #Subcategoria
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank= True) #Autor models.ForeignKey(User, on_delete=models.CASCADE) <- ¡Si borramos al autor va a borrar por cascada los posteos realizados por el mismo!
    body = models.TextField(max_length=9600) #Cuerpo
    publication_date = models.DateTimeField(auto_now=True) #Fecha de publicacion


    def __str__(self):
        return f"{self.title} | {self.author} | {self.publication_date}"

#Falta crear la imagen de la clase Publication


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=True) #ID comentarista #Debe pegar con el ID usuario investigar foreign key / clave foranea
    commenter_name = models.CharField(max_length=200) #Nombre comentarista
    comment_body = models.TextField(max_length=300) #Cuerpo de comentario     ¡OJO ForeingKey de adentro hacia afuera! 


#Crear un model Categoria -> relacion mucho a muchos o uno a muchos 
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return f"{self.category_name}"

#CLASE CON PERFIL - CONSULTA DE ID PARA CONEXION 