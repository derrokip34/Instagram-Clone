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
