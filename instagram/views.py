from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Image,UserProfile

# Create your views here.

def home(request):
    images = Image.get_all_images()

    title = 'Welcome to Instagram'
    return render(request, 'index.html',{'title':title,'images':images})

@login_required()
def profile(request,username):
    profile = User.objects.get(username=username)
    try:
        profiles = UserProfile.get_by_id(profile.id)
    except:
        profiles = UserProfile.filter_by_id(profile.id)
    images = Image.get_profile_images(profile.id)
    return render(request, 'profile.html', {'images': images,"profile":profile,"profiles":profiles})
