from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Image,Profile
from .forms import UpdateProfile,UpdateUser,PostImageForm
from django.conf.urls import url

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
    current_user = request.user
    if request.method == 'POST':
        u_form = UpdateUser(request.POST,instance=request.user)
        p_form = UpdateProfile(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('userProfile',id=current_user.id)

    else:
        u_form = UpdateUser(instance=request.user)
        p_form = UpdateProfile(instance=request.user.profile)

    title = f'Update @{current_user.username} profile'
    return render(request,'update_profile.html', {'title':title,'user_form':u_form,'profile_form':p_form})

@login_required(login_url='/accounts/login')
def post_image(request):
    current_user = request.user
    if request.method == 'POST':
        img_form = PostImageForm(request.POST,request.FILES)
        if img_form.is_valid():
            image = img_form.save(commit=False)
            image.owner = current_user
            image.profile = current_user.profile
            image.save()
        return redirect('home')
    else:
        img_form = PostImageForm()

    title = 'New Post'
    return render(request, 'new_post.html',{'title':title,'img_form':img_form})