from django.contrib import admin
from .models import UserProfile,Image,Comments

# Register your models here.
admin.site.register(Image)
admin.site.register(Comments)
admin.site.register(UserProfile)