from django.urls import path
from appBlog.views import  see_publication, home, add_publication

urlpatterns = [
    
    path('publications/', see_publication, name = 'publication'),
    path('home/', home, name = 'home'),
    path('publicationForm/', add_publication, name='addPublication'),
    #Acá van las URLS de los las vistas y templates a conectar
]