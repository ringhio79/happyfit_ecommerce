from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['full_name', 'phone_number', 'gender', 'country', 'postcode', 'town_or_city', 'street_address_1', 'street_address_2', 'county']
        
