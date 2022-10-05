from django.urls import path
from appBlog.views import  seePublications, seePublication, home, homeLogin, about, addPublication, register, seeUsers, loginRequest, addComment, deleteComment, updateComment, addCategory, seeCategories, deleteCategory, updateCategory, updatePublication,  deletePublication
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    #Home path
    path('home/', home, name = 'home'),
    path('homeLogin/', homeLogin, name='homeLogin'),
    path('about/', about, name='about'),
    #Publication
    path('publications/', seePublications, name = 'publication'),
    path('publication/<id>', seePublication, name ='seePublication'),
    path('publicationForm/', addPublication, name='addPublication'),
    path('updatePublication/<id>', updatePublication, name='updatePublication'),
    path('deletePublication/<id>', deletePublication, name='deletePublication'),
    #Users
    path('seeUsers/' ,seeUsers, name= "users"),

    #Commenters
    path('commentForm/<publication_id>', addComment, name='addComment'),
    path('updateComment/<id>', updateComment, name='updateComment'),
    path('deleteComment/<id>', deleteComment, name='deleteComment'),
    
    #Categories
    path('categoryForm/', addCategory, name='addCategory'),
    path('seeCategories/', seeCategories, name='categories'),
    path('deleteCategory/<id>', deleteCategory, name='deleteCategory'),
    path('updateCategory/<id>', updateCategory, name='updateCategory'),

    #Register,Login and logout
    path('userRegister/', register, name= 'register'),
    path('login/', loginRequest, name='login'),
    path('logout/', LogoutView.as_view(template_name ='appblog/logout.html'), name='logout'),


]