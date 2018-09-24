from django.test import TestCase
from .forms import ProfileForm

# Create your tests here.
class TestDjango(TestCase):
    
    def test_is_this_thing_on(self):
        self.assertEqual(1, 1)
        

    def test_profile_form_valid(self):
        form = ProfileForm({
            'first_name': 'daisy',
            'last_name': 'duck',
            'profile_image': 'avatars/anonymous.png',
            'gender': 'FEMALE',
            'house_no': '55',
            'street_name': 'simple street',
            'town_or_city': 'norfolk',
            'postcode': 'nxr45',
            'county': 'berkshire',
            'country': 'england',
        })
 
        self.assertTrue(form.is_valid())
