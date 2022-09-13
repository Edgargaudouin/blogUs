from django.urls import path
from appBlog.views import  publication, home, user

urlpatterns = [
    
    path('publications/', publication, name = 'publication'),
    path('home/', home, name = 'home'),
    path('users/', user, name = 'user'),
    #Acá van las URLS de los las vistas y templates a conectar
]