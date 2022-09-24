from django.shortcuts import render, get_object_or_404, redirect
from appBlog.models import *
from appBlog.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'appblog/home.html')

@login_required
def homeLogin(request):
    return render(request, 'appblog/homeLogin.html')


############################# PUBLICATION ###############################
#CREATE

@login_required
def add_publication(request):

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
            return render (request, 'appblog/home.html', {'message': "Publicacion creada"})
        else:                      #Si el formulario no puede ser validado
            return render (request, 'appblog/home.html', {'message':"Error"})
    else:
        form = PublicationForm()   #Medoto GET envia el formulario vacio
        return render (request, 'appblog/publication/publicationForm.html', {'formulary' : form})

#READ
@login_required
def see_publication(request):
    publication = Publication.objects.all()
    return render(request, 'appblog/publication/publications.html', {'publication' : publication })

#UPDATE

#DELETE

############################# CATEGORY ###############################
#CREATE
def add_category(request):
    if request.method =='POST':
        form = CategoryForm(request.POST)     #CREAR   
          #  fields = ['title', 'caption','sub_category','body']
        if form.is_valid():
            data = form.cleaned_data 
            category_name = data['category_name']
        
            cate = Category( category_name=category_name)
            cate.save()
            return render (request, 'appblog/home.html', {'message': "¡Categoria creada!"})
        else:                      #Si el formulario no puede ser validado
            return render (request, 'appblog/home.html', {'message':"Error"})
    else:
        form = CategoryForm()   #Medoto GET envia el formulario vacio
        return render (request, 'appblog/category/categoryForm.html', {'formulary' : form})
#READ
@login_required
def see_categories(request):
    categories = Category.objects.all()
    return render(request, 'appblog/category/categories.html', {'categories' : categories })
#UPDATE
#DELETE

############################# COMMENT ###############################
#CREATE

@login_required
def add_comment(request):
    if request.method =="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.save()
        else:
            return render(request, 'appblog/home.html', {'message': "Error al comentar la publicación"})
    else: 
        form = CommentForm()
        return render(request, 'appblog/comment/commentForm.html', {'formulary' : form})


@login_required
def add_comment(request):
    if request.method =="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment_body = data['comment_body']
            commen = Comment(comment_body=comment_body)
            commen.save()
            return redirect(add_comment, id)
        else:
            return render(request, 'appblog/home.html', {'message': "Error al comentar la publicación"})
    else: 
        form = CommentForm()
        return render(request, 'appblog/comment/commentForm.html', {'formulary' : form})






#READ
#UPDATE
#DELETE


@login_required
def see_users(request):
    users = User.objects.all().values()
    name_list = []
 
    for item in users:
        item.values()
        name_list.append(item)
    return name_list
       
       
    print(name_list)
    print(users)
    print(f_name_list)
    return render(request, 'appblog/user/users.html', {'users' : name_list })


############################# LOGIN ###############################

def login_request(request):
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
                return render(request, 'appblog/home.html', {"message":"Error, datos incorrectos"} )
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
            return render(request, 'appblog/home.html', {'mensaje':"Usuario creado"})
        else:
            return render(request, 'appblog/user/userRegister.html', {'mensaje':"Error: ¡Ingresó datos invalidos!"})
    else:
        form=UserRegisterForm()
    return render(request, 'appblog/user/userRegister.html', {'form':form})