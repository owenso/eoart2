from django.db import models

# Create your models here.

ARTWORK_TYPES = (
    ('ac', 'Acrylic'),
    ('photo', 'Photograph'),
    ('wc', 'Watercolor')
)


class Artwork(models.Model):
    artwork_type = models.CharField(choices=ARTWORK_TYPES, max_length=5)
    image = models.ImageField(upload_to='shows/', null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    def __str__(self):
        return self.name
