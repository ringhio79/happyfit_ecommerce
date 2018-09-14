from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(blank=False, null=False)
    capacity = models.IntegerField(default=0)
    theme = models.CharField(max_length=30, blank=True, null=True)
    instructor = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    
    def __str__(self):
        return self.event_name
        
class Booking(models.Model):
    user = models.CharField(max_length=200, default=1)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.user

class Ticket(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    member = models.ForeignKey(User, related_name='tickets', null=False, default=1, on_delete=models.SET_DEFAULT)
    event = models.ForeignKey(Event, related_name='tickets', null=False, default=1, on_delete=models.SET_DEFAULT)
    booking = models.ForeignKey(Booking, related_name='tickets', null=False, default=1, on_delete=models.SET_DEFAULT)
    
    def __str__(self):
        return self.member.username
        
        
