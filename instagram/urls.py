from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^profile/id/(?P<id>\d+)',views.profile,name='userProfile'),
    url(r'^update_profile/',views.update_profile,name='update'),
    url(r'^post_image/',views.post_image,name='newPost'),
    url(r'^comment/id/(?P<image_id>\d+)',views.comment,name='comment')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)