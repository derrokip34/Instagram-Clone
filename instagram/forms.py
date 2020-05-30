from django import forms
from .models import UserProfile,Image,Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=60,help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm')

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']

class PostImage(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['image', 'user']