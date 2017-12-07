from django.db import models

# Create your models here.

# ARTWORK_TYPES = (
#     ('ac', 'Acrylic'),
#     ('ph', 'Photograph'),
#     ('wc', 'Watercolor')
# )


# class Category(models.Model):
#     name = models.CharField(max_length=50)
#     desc = models.TextField()

class Artwork(models.Model):
    # category = models.ManyToManyField(Category)
    # artwork_type = models.CharField(choices=ARTWORK_TYPES, max_length=5)
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
