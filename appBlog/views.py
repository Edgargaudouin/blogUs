from email import message
import email
from optparse import Values
from unicodedata import category
from django.shortcuts import render
from appBlog.models import *
from appBlog.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse


def home(request):
    publications = Publication.objects.all()
    return render(request, 'appblog/home.html',{'publications' : publications })

@login_required
def homeLogin(request):
    return render(request, 'appblog/homeLogin.html')

############################# ABOUT ###############################
def about(request):
    is_loged = bool(request.user.username)
    return render(request, 'appblog/about.html', {'is_loged':is_loged})

############################# PUBLICATION ###############################
#CREATE
@login_required
def addPublication(request):
    if request.method =='POST':
       
        form = PublicationForm(request.POST, request.FILES)     #CREAR   
          #  fields = ['title', 'caption','sub_category','body']
        if form.is_valid():
            data = form.cleaned_data 
            title = data['title']
            caption = data['caption']
            sub_category = data['sub_category']
            body = data['body']
            category = data['category']
            image = data['image']
            publi = Publication( title=title, caption=caption,category=category, sub_category=sub_category,author=User(request.user.id), body=body, image=image)
            publi.save()
            return render (request, 'appblog/homeLogin.html', {'message': "Publicacion creada"})
        else:                      
            return render (request, 'appblog/homeLogin.html', {'message':"Error"})
    else:
        form = PublicationForm()   
        return render (request, 'appblog/publication/publicationForm.html', {'formulary' : form})

#READ
@login_required
def seePublications(request):
    publications = Publication.objects.all()
    return render(request, 'appblog/publication/publications.html', {'publications' : publications })

@login_required #Visualizaci??n en detalle de la publicaci??n 
def seePublication(request, id):
    publication = Publication.objects.get(id=id)
    return render(request, 'appblog/publication/publication.html', {'publication' : publication})

#UPDATE
@login_required
def updatePublication(request, id):
    publication = Publication.objects.get(id=id)
    loger_user = request.user
    publication_author = publication.author
    if loger_user == publication_author:
        if request.method=="POST":
            form=PublicationForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                publication.title = data["title"]
                publication.caption = data["caption"]
                publication.sub_category = data["sub_category"]
                publication.body = data["body"]
                publication.image = data["image"]
                publication.save()
                publications = Publication.objects.all()
                return render(request, 'appblog/publication/publications.html',{'publications':publications, 'message':'Publicacion actualizada'})
            else:
                return render(request, 'appblog/publication/publications.html',{'message':'ERROR'})
        else:
            form = PublicationForm(initial={'title':publication.title,'caption':publication.caption,'sub_category':publication.sub_category, 'body':publication.body, 'image':publication.image })
        return render(request, 'appblog/publication/edit.html', {'form':form, 'publication.title':publication.title, 'id':publication.id} )
    else:
        return render(request, 'appblog/homeLogin.html', {'message':'Error: usuario sin autorizaci??n para editar esta publicaci??n'} )

#DELETE
@login_required
def deletePublication(request, id):
    publication = Publication.objects.get(id=id)
    loger_user = request.user
    publication_author = publication.author
    if loger_user == publication_author:
        publication = Publication.objects.get(id=id).delete()
        publications = Publication.objects.all()
        return render(request, 'appblog/publication/publications.html',{'publications':publications, 'message':'Publicacion borrada'})
    else:
        return render(request, 'appblog/homeLogin.html', {'message':'Error: usuario sin autorizaci??n para eliminar esta publicaci??n'} )       
 
############################# CATEGORY ###############################
#CREATE
@login_required
def addCategory(request):
    if request.method =='POST':
        form = CategoryForm(request.POST)    
        if form.is_valid():
            data = form.cleaned_data 
            category_name = data['category_name']
            cate = Category( category_name=category_name)
            cate.save()
            return render (request, 'appblog/homeLogin.html', {'message': "??Categoria creada!"})
        else:                     
            return render (request, 'appblog/homeLogin.html', {'message':"Error"})
    else:
        form = CategoryForm()  
        return render (request, 'appblog/category/categoryForm.html', {'formulary' : form})
#READ
@login_required
def seeCategories(request):
    categories = Category.objects.all()
    return render(request, 'appblog/category/categories.html', {'categories':categories})

#UPDATE
@staff_member_required
def updateCategory(request, id):
    category = Category.objects.get(id=id)
    if request.method=="POST":
        form=CategoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            category.category_name = data['category_name']
            category.save()
            categories = Category.objects.all()
            return render(request, 'appblog/category/categories.html', {'categories':categories, 'message': 'Categoria actualizada'})
    else:
        form = CategoryForm(initial={'category_name':category.category_name})
        return render(request, 'appblog/category/edit.html', {'form':form, 'category.category_name':category.category_name, 'id':category.id} )

#DELETE
@staff_member_required
def deleteCategory(request, id):
    category=Category.objects.get(id=id).delete()
    superusers = User.objects.filter(is_superuser=True)
    categories=Category.objects.all()
  
    return render(request,'appblog/category/categories.html', {'categories':categories,'message':'Categoria eliminada' })
    
############################# COMMENT ###############################
#CREATE
@login_required
def addComment(request, id):
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            body = data['body']
            comm = Comment(username=User(request.user.id), body=body, publication=Publication(id))
            comm.save()
            return render(request, 'appblog/publication/publications.html', {'message': 'Comentario realizado'})
        else:
            return render(request, 'appblog/publication/publications.html', {'message':'Error al realizar el comentario'})
    else:
        form = CommentForm()
        return render(request, 'appblog/comment/commentForm.html',{'form':form , 'id':id})

#UPDATE
@login_required
def updateComment(request, id):
    comment = Comment.objects.get(id=id)
    loger_user = request.user
    comment_author = comment.username
    if loger_user == comment_author:
        if request.method=='POST':
            form=CommentForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                comment.body = data['body']
                comment.save()
                comments = Comment.objects.all()
                return render(request, 'appblog/publication/publications.html', {'message':'Comentario actualizado'})
        else:
            form = CommentForm(initial={'body':comment.body})
            return render(request, 'appblog/comment/edit.html', {'form':form, 'comment.body':comment.body, 'id': comment.id})
    
    else:
        return render(request, 'appblog/publication/publications.html', {'message':'Usuario no habilitado'})
#DELETE 
@login_required
def deleteComment(request, id):
    comment = Comment.objects.get(id=id)
    loger_user = request.user
    comment_author = comment.username
    if loger_user == comment_author:
        comment = Comment.objects.get(id=id).delete()
        comments = Comment.objects.all()
        return render(request, 'appblog/publication/publications.html',{'comments':comments, 'message':'Comentario eliminado'})
    else:
        return render(request, 'appblog/homeLogin.html', {'message':'Error: usuario sin autorizaci??n para eliminar esta publicaci??n'} )       
 

############################# USER ###############################

@login_required
def seeUsers(request):
    users = User.objects.all()
    return render(request, 'appblog/user/users.html', {'users' : users })

@login_required
def updateUser(request, id):
    user = User.objects.get(id=id)
    if request.method=='POST':
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
           
            usernames_in_use = User.objects.filter(username=User.username)
            emails_in_use = User.objects.filter(email=User.email)
            if username in usernames_in_use:
                return render(request, 'appblog/homeLogin.html', {'message':'Error: El nombre de usuario ingresado ya est?? siendo utilizado'} )
            elif email in emails_in_use:
                return render(request, 'appblog/homeLogin.html', {'message':'Error: El email ingresado ya est?? siendo utilizado'} )
            else:
                user.first_name = first_name
                user.last_name= last_name
                user.username = username
                user.email = email
                user.set_password(password)
                user.save()
                print(password)
                login(request, user)
                return render(request, 'appblog/user/edit.html', {'message':"Usuario actualizado", 'id':id})
        else:
            return render(request, 'appblog/user/edit.html', {'message':"Error: ??Ingres?? datos invalidos!",'form':form, 'id':id})
    else:
        form=UserUpdateForm()
    return render(request, 'appblog/user/edit.html', {'form':form,'id':id})
 


@login_required
def deleteUser(request, id):
    user = User.objects.get(id=id)
    loger_user = request.user
    print(loger_user)
    print(user.username)
    if loger_user == user:
        user.delete()
        return render(request, 'appblog/home.html',{ 'message':'El usuario ha sido eliminado'})
    else:
        return render(request, 'appblog/homeLogin.html', {'message':'Error: usuario sin autorizaci??n para eliminar este usuario'} )   

############################# LOGIN ###############################
def loginRequest(request):
    if request.method == "POST":
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, 'appblog/homeLogin.html', {"message":f"Bienvenido {user}"})
            else:
                return render(request, 'appblog/homeLogin.html', {"message":"Error, datos incorrectos"} )
        else:
            return render(request, 'appblog/home.html', {"message":"Error: formulario erroneo"})
    else:
        form = LoginForm()
        return render(request, 'appblog/login.html', {"form":form})

############################# REGISTER ###############################
def register(request):
    if request.method=="POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            
            #podriamos fijarnos que no exista un user en la bd con ese nombre
            form.save()
            return render(request, 'appblog/user/userRegister.html', {'message':"Usuario creado"})
        else:
            return render(request, 'appblog/user/userRegister.html', {'message':"Error: ??Ingres?? datos invalidos!"})
    else:
        form=UserRegisterForm()
    return render(request, 'appblog/user/userRegister.html', {'form':form})