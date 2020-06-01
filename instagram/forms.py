from django import forms
from .models import Profile,Image,Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio']

class UpdateUser(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

class PostImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image','image_name','image_caption']