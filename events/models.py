from django.db import models
from django.utils import timezone

# Create your models here.

class CurrentShow(models.Model):
    # created_by = models.ForeignKey('auth.User')
    address = models.CharField(max_length=255, blank=True)
    venue_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    startDate = models.DateTimeField(blank=True, null=True)
    endDate = models.DateTimeField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    show_image = models.ImageField(upload_to='shows/', blank=True, null=True)

    def __str__(self):
        return self.venue_name

class PreviousVenue(models.Model):
    # created_by = models.ForeignKey('auth.User')
    venue_name = models.CharField(max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta(object):
        ordering = ['venue_name']

    def __str__(self):
        return self.venue_name
