from unicodedata import category
from django.shortcuts import render
from appBlog.models import *
from appBlog.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def home(request):
    return render(request, 'appblog/home.html')

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
        form = PublicationForm(request.POST)     #CREAR   
          #  fields = ['title', 'caption','sub_category','body']
        if form.is_valid():
            data = form.cleaned_data 
            title = data['title']
            caption = data['caption']
            sub_category = data['sub_category']
            body = data['body']
           
            publi = Publication( title=title, caption=caption, sub_category=sub_category,author=User(request.user.id), body=body) 
            publi.save()
            return render (request, 'appblog/homeLogin.html', {'message': "Publicacion creada"})
        else:                      #Si el formulario no puede ser validado
            return render (request, 'appblog/homeLogin.html', {'message':"Error"})
    else:
        form = PublicationForm()   #Medoto GET envia el formulario vacio
        return render (request, 'appblog/publication/publicationForm.html', {'formulary' : form})

#READ
@login_required
def seePublication(request):

    publication = Publication.objects.all()
    return render(request, 'appblog/publication/publications.html', {'publication' : publication })

#UPDATE
@login_required
def updatePublication(request, id):
    publication = Publication.objects.get(id=id)
    
    loger_user = request.user
    publication_author = publication.author
    if loger_user == publication_author:
        if request.method=="POST":
            form=PublicationForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                publication.title = data["title"]
                publication.caption = data["caption"]
                publication.sub_category = data["sub_category"]
                publication.body = data["body"]
                publication.save()
                publications = Publication.objects.all()
                return render(request, 'appblog/publication/publications.html',{'publications':publications, 'message':'Publicacion actualizada'})
        else:
            form = PublicationForm(initial={'title':publication.title,'caption':publication.caption,'sub_category':publication.sub_category, 'body':publication.body })
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
        form = CategoryForm(request.POST)     #CREAR   
          #  fields = ['title', 'caption','sub_category','body']
        if form.is_valid():
            data = form.cleaned_data 
            category_name = data['category_name']
        
            cate = Category( category_name=category_name)
            cate.save()
            return render (request, 'appblog/homeLogin.html', {'message': "¡Categoria creada!"})
        else:                      #Si el formulario no puede ser validado
            return render (request, 'appblog/homeLogin.html', {'message':"Error"})
    else:
        form = CategoryForm()   #Medoto GET envia el formulario vacio
        return render (request, 'appblog/category/categoryForm.html', {'formulary' : form})
#READ
@login_required
def seeCategories(request):
    categories = Category.objects.all()
    return render(request, 'appblog/category/categories.html', {'categories' : categories })
#UPDATE
@login_required
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
@login_required
def deleteCategory(request, id):
    category=Category.objects.get(id=id).delete()
    categories=Category.objects.all()
    return render(request, 'appblog/category/categories.html',{'categories':categories})


############################# COMMENT ###############################
#CREATE
@login_required
def addComment(request):
    if request.method =="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment_body = data['comment_body']
            commen = Comment(comment_body=comment_body)
            commen.save()
            return redirect(add_comment, id)
        else:
            return render(request, 'appblog/homeLogin.html', {'message': "Error al comentar la publicación"})
    else: 
        form = CommentForm()
        return render(request, 'appblog/comment/commentForm.html', {'formulary' : form})

#READ
#UPDATE
#DELETE


@login_required
def seeUsers(request):
    users = User.objects.all()
    return render(request, 'appblog/user/users.html', {'users' : users })
    

############################# LOGIN ###############################
def loginRequest(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
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
        form = AuthenticationForm()
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