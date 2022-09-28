from django.urls import path
from appBlog.views import  see_publication, home, homeLogin, add_publication, register, see_users, login_request, add_comment, add_category, see_categories, deleteCategory, updatePublication,  deletePublication
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    #Home path
    path('home/', home, name = 'home'),
    path('homeLogin/', homeLogin, name='homeLogin'),
    #Publication
    path('publications/', see_publication, name = 'publication'),
    path('publicationForm/', add_publication, name='addPublication'),
    
    path('updatePublication/<id>', updatePublication, name='updatePublication'),
    path('deletePublication/<id>', deletePublication, name='deletePublication'),
 
    path('seeUsers/' ,see_users, name= "users"),
    path('commentForm/', add_comment, name='addComment'),

    #Categories
    path('categoryForm/', add_category, name='addCategory'),
    path('seeCategories/', see_categories, name='categories'),
    path('deleteCategory/<id>', deleteCategory, name='deleteCategory'),

    #Register,Login and logout
    path('userRegister/', register, name= 'register'),
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name ='appblog/logout.html'), name='logout'),


]