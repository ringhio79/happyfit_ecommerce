from django.db import models
from django.utils import timezone



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