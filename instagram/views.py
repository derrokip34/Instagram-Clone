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
def profile(request,username):
    user = User.objects.filter(username=username).first()
    
    return render(request, 'profile.html',{'user':user})