from django import forms
from django.contrib.auth.models import User
from appBlog.models import *
from django.contrib.auth.forms import UserCreationForm



class PublicationForm(forms.ModelForm):
    
    class Meta:
        model = Publication
        fields = ['title','caption','sub_category','body']

 

class UserRegisterForm(UserCreationForm):

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}




class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['comment_body']


