from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['first_name', 'last_name', 'image', 'gender', 'street_address_1', 'street_address_2','town_or_city', 'postcode', 'county', 'country']
        
