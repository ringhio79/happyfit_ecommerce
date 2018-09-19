from .models import Event
from django import forms
import django_filters

class CategoryFilter(django_filters.FilterSet):
    
    class Meta:
        model = Event
        fields = ['category']