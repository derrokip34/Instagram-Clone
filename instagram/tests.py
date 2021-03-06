from django.test import TestCase
from .models import Image,Profile,Comments
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTests(TestCase):
    
    def setUp(self):
        self.user = User(id=1,username='derrick',email='derrick@gmail.com',password='58744')
        self.user.save()
        self.profile = Profile(user_id=1,bio='Cool cool cool No doubt no doubt no doubt',profile_pic='b99.jpg')
        self.profile.save()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_isinstance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete_profile(self):
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)==0)

    def test_get_by_id(self):
        self.profile.save_profile()
        profile = Profile.get_by_id(1)
        self.assertEqual(profile.user_id,1)

class ImageTests(TestCase):
    def setUp(self):
        self.user = User(id=1,username='derrick',email='derrick@gmail.com',password='58744')
        self.user.save()
        self.profile = Profile(user_id=1,bio='Cool cool cool No doubt no doubt no doubt',profile_pic='b99.jpg')
        self.profile.save()
        self.img = Image(image='b99.jpg',image_name='Brooklyn 99',image_caption='Brooklyn 99 season 7 Poster',date_posted='2020-06-04',likes=1000,owner=self.user,profile=self.profile)
        self.img.save_image()

    def tearDown(self):
        Image.objects.all().delete()

    def test_isinstance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.img,Image))

    def test_save_image_method(self):
        self.img.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_image(self):
        self.img.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)

    def test_get_all_images(self):
        images = Image.get_all_images()
        self.assertTrue(len(images)>0)

class CommentsTests(TestCase):
    def setUp(self):
        self.user = User(id=1,username='derrick',email='derrick@gmail.com',password='58744')
        self.user.save()
        self.profile = Profile(user_id=1,bio='Cool cool cool No doubt no doubt no doubt',profile_pic='b99.jpg')
        self.profile.save()
        self.img = Image(image='b99.jpg',image_name='Brooklyn 99',image_caption='Brooklyn 99 season 7 Poster',date_posted='2020-06-04',likes=1000,owner=self.user,profile=self.profile)
        self.img.save_image()
        self.comment = Comments(image=self.img,comment="Can't wait for the next season of th Nine Nine",user=self.user,date_posted='2020-06-04')
        self.comment.save_comment()

    def tearDown(self):
        Comments.objects.all().delete()

    def test_isinstance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.img,Image))
        self.assertTrue(isinstance(self.comment,Comments))

    def test_save_comment_method(self):
        self.comment.save_comment()
        comments = Comments.objects.all()
        self.assertTrue(len(comments)>0)

    def test_delete_comment(self):
        self.comment.delete_comment()
        comments = Comments.objects.all()
        self.assertTrue(len(comments)==0)
