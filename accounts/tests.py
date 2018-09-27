from django.test import TestCase
from .models import Profile
from .forms import ProfileForm

# Create your tests here.
class TestDjango(TestCase):
        
    def test_profile_form_valid(self):
        form = ProfileForm({
            'first_name': 'daisy',
            'last_name': 'duck',
            'profile_image': 'avatars/anonymous.png',
            'gender': 'F',
            'house_no': '55',
            'street_name': 'simple street',
            'town_or_city': 'norfolk',
            'postcode': 'nxr45',
            'county': 'berkshire',
            'country': 'england',
        })

        self.assertTrue(form.is_valid())
        
    def test_profile_form_valid_mandatory_fields(self):
        form = ProfileForm({
            'first_name': 'test',
            'last_name': 'testone',
            'profile_image': 'avatars/anonymous.png',
            'gender': 'F',
            'house_no': '55',
            'street_name': 'test street',
            'town_or_city': 'norfolk',
            'country': 'england',
        })
        self.assertTrue(form.is_valid())
    
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
        
            
