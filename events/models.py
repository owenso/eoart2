from django.db import models
from django.utils import timezone

# Create your models here.

class CurrentShow(models.Model):
    # created_by = models.ForeignKey('auth.User')
    address = models.CharField(max_length=255, blank=True)
    venue_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    show_image = models.ImageField(upload_to='shows/', blank=True, null=True)

    class Meta(object):
        verbose_name_plural = "Current Shows"

    def __str__(self):
        return self.venue_name

class PreviousVenue(models.Model):
    # created_by = models.ForeignKey('auth.User')
    venue_name = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta(object):
        ordering = ['venue_name']
        verbose_name_plural = "Previous Venues"

    def __str__(self):
        return self.venue_name
