from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Image,Profile

# Create your views here.

@login_required(login_url='/accounts/login')
def home(request):
    images = Image.get_all_images()

    title = 'Welcome to Instagram'
    return render(request, 'index.html',{'title':title,'images':images})

@login_required(login_url='/accounts/login')
def profile(request,id):
    user = User.objects.filter(id=id).first()
    user_profile = user.profile
    profile = Profile.get_by_id(id)
    images = Image.get_profile_images(id)
    
    title = f'@{user.username} Instagram photos'
    return render(request, 'profile.html',{'user':user,'profile':user_profile,"images":images,'title':title})