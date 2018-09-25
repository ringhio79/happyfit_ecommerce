from django.test import TestCase
from .models import Profile

# Create your tests here.
class TestDjango(TestCase):
        

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "events/home.html")
        
    def view_editprofile_by_user(self):
        profile = Profile({
            'first_name': 'test',
            'last_name': 'testone',
            'profile_image': 'avatars/anonymous.png',
            'gender': 'F',
            'house_no': '55',
            'town_or_city': 'norfolk',
            'country': 'england',
        })
        profile.save()
        
        page = self.client.get("/edit/{0}".format(profile.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "accounts/profile_form.html")
        
        
        
