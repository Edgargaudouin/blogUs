from django.urls import path
from appBlog.views import  see_publication, home

urlpatterns = [
    
    path('publications/', see_publication, name = 'publication'),
    path('home/', home, name = 'home'),
   
    #Acá van las URLS de los las vistas y templates a conectar
]