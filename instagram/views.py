from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Image,Profile
from .forms import UpdateProfile,UpdateUser

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

@login_required(login_url='/accounts/login')
def update_profile(request):
    if request.method == 'POST':
        u_form = UpdateUser(request.POST,instance=request.user)
        p_form = UpdateProfile(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('home')

    else:
        u_form = UpdateUser(instance=request.user)
        p_form = UpdateProfile(instance=request.user.profile)


    return render(request,'update_profile.html', {'user_form':u_form,'profile_form':p_form})