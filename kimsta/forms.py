from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import posts,Profile,Comment

class ImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={

        'id': 'imageform', 'class': 'uploadimage'

    }))

    class Meta:
        model = posts
        fields = ['image','title','caption']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment        
        fields=['comment']   

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']