from email import message
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
    return render(request, 'appblog/about.html')

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

@login_required #Visualización en detalle de la publicación 
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
        return render(request, 'appblog/homeLogin.html', {'message':'Error: usuario sin autorización para editar esta publicación'} )

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
        return render(request, 'appblog/homeLogin.html', {'message':'Error: usuario sin autorización para eliminar esta publicación'} )       
 
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
            return render (request, 'appblog/homeLogin.html', {'message': "¡Categoria creada!"})
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
def addComment(request, publication_id):
    if request.method=='POST':
        form = CommentForm(request.POST)
        user_id = User.objects.get(username=request.user.username)
        if form.is_valid():
            data=form.cleaned_data
            body=data['body']
            commen = Comment(username=user_id, body=body, publication=Publication(publication_id))
            commen.save()
            return render(request, 'appblog/publication/publications.html', {'message': 'Comentario realizado'})
        else:
            return render(request, 'appblog/publication/publications.html', {'message':'Error al realizar el comentario'})
    else:
        form = CommentForm()
        return render(request, 'appblog/comment/commentForm.html',{'form':form, 'publication_id':publication_id})
#UPDATE
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
def deleteComment(request, id):
    comment = Comment.objects.get(id=id)
    loger_user = request.user
    comment_author = comment.username
    if loger_user == comment_author:
        comment = Comment.objects.get(id=id).delete()
        comments = Comment.objects.all()
        return render(request, 'appblog/publication/publications.html',{'publications':comments, 'message':'Comentario eliminado'})
    else:
        return render(request, 'appblog/homeLogin.html', {'message':'Error: usuario sin autorización para eliminar esta publicación'} )       
 

############################# USER ###############################

@login_required
def seeUsers(request):
    users = User.objects.all()
    return render(request, 'appblog/user/users.html', {'users' : users })

@login_required
def updateUser(request, id):
    pass

@login_required
def deleteUSer(request, id):
    pass

    

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
            return render(request, 'appblog/user/userRegister.html', {'message':"Error: ¡Ingresó datos invalidos!"})
    else:
        form=UserRegisterForm()
    return render(request, 'appblog/user/userRegister.html', {'form':form})