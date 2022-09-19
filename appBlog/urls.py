from django.urls import path
from appBlog.views import  see_publication, home, add_publication, register, see_users, login_request
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('publications/', see_publication, name = 'publication'),
    path('home/', home, name = 'home'),
    
    path('publicationForm/', add_publication, name='addPublication'),
    path('userRegister/', register, name= 'register'),
    path('seeUsers/' ,see_users, name= "users"),

    #Login
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name ='appblog/logout.html'), name='logout'),

    #Acá van las URLS de los las vistas y templates a conectar
]