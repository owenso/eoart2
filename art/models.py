from django.db import models

# Create your models here.

class Artwork(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order']
        verbose_name_plural = "artwork"

    def __str__(self):
        return self.name


class Acrylic(Artwork):
    image = models.ImageField(upload_to='artwork/ac/', null=True)
class Photograph(Artwork):
    image = models.ImageField(upload_to='artwork/ph/', null=True)
class Watercolor(Artwork):
    image = models.ImageField(upload_to='artwork/wc/', null=True)
