from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    GENDER_LIST = (
        ('F', 'FEMALE'),
        ('M', 'MALE'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_image = models.ImageField(upload_to="avatars", null=False, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_LIST, blank=False, null=False)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    house_no = models.CharField(max_length=40, blank=False)
    street_name = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=True)
    stripe_id = models.CharField(max_length=80, blank=True, null=True)
    subscription_id = models.CharField(max_length=80, blank=True, null=True)
    
    def __str__(self):
        return self.user.username + ' Profile'