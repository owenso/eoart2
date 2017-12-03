from django.db import models
from django.utils import timezone

# Create your models here.

class Shows(models.Model):
    created_by = models.ForeignKey('auth.User')
    address = models.CharField(max_length=255, blank=True)
    venue_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    show_image = models.ImageField(upload_to='shows/', null=True)
