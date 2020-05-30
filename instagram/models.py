from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='media/')
    image_name = models.CharField(max_length=60)
    image_caption = models.CharField(max_length=60)
    profile = models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def save_image(self):
        self.save()

    @classmethod
    def get_profile_images(cls,profile):
        images = Image.objects.filter(profile__pk = profile)
        return images

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

class Comments(models.Model):
    image = models.ForeignKey('Image',on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

class UserProfile(models.Model):
    profile_pic = models.ImageField(upload_to='media/')
    bio = models.CharField(max_length=100,default="I'm new to Instagram")
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    def save_profile(self):
        self.save()

    @classmethod
    def search_user(cls,search_term):
        profiles = cls.objects.filter(user__icintains=search_term)
        return profiles

    @classmethod
    def get_by_id(cls,id):
        profile = UserProfile.objects.get(user=id)
        return profile

    @classmethod
    def filter_by_id(cls,id):
        profile = UserProfile.objects.filter(user = id).first()
        return profile