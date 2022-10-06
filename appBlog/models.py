from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.

#Crear un model Categoria -> relacion mucho a muchos o uno a muchos 
class Category(models.Model):
    category_name = models.CharField(max_length=200)
  

    def __str__(self):
        return f"{self.category_name}"

class Publication(models.Model):
   
    title = models.CharField(max_length=60) #Titulo
    caption = models.CharField(max_length=60) #Subtitulo
    category = models.ForeignKey(Category, on_delete = models.CASCADE) 
    sub_category = models.CharField(max_length=20) #Subcategoria
    author = models.ForeignKey(User, on_delete=models.CASCADE, null =False, blank=False) #Autor models.ForeignKey(User, on_delete=models.CASCADE) <- ¡Si borramos al autor va a borrar por cascada los posteos realizados por el mismo!
    body = RichTextField(blank=True, null=True)
    publication_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='publications', null = True, blank = True) 


    def __str__(self):
        return f"{self.title} | {self.author} | {self.publication_date}"

#Falta crear la imagen de la clase Publication


class Comment(models.Model):
    
    username = models.ForeignKey(User,on_delete=models.CASCADE ) #Nombre comentarista
    body = RichTextField(blank=True, null=True)    
    publication = models.ForeignKey(Publication, related_name="comments", on_delete=models.CASCADE, null =False, blank=False) #Uso el related_name para relacionarlo con el template publications.html
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comentado por {self.username}'
        


#CLASE CON PERFIL - CONSULTA DE ID PARA CONEXION 
