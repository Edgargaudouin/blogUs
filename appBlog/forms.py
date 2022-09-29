from django import forms
from django.contrib.auth.models import User
from appBlog.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class PublicationForm(forms.ModelForm):
    
    class Meta:
        model = Publication
        fields = ['title','caption','category','sub_category','body']

 

class UserRegisterForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'label':'contraseña'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'label':'confirmar contraseña'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', }),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }




class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'label':'Usuario'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'label':'contraseña'}),
    )










class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['body']
     


class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['category_name']