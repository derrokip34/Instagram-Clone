from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='media/')
    image_name = models.CharField(max_length=60)
    image_caption = models.CharField(max_length=60)
    likes = models.IntegerField(default=0)

class Comments(models.Model):
    image = models.ForeignKey('Image',on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)

class UserProfile(models.Model):
    profile_pic = models.ImageField(upload_to='media/')
    bio = models.CharField(max_length=100,default="I'm new to Instagram")
    user = models.OneToOneField(User,on_delete=models.CASCADE)