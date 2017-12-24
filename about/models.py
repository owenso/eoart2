from django.db import models

# Create your models here.


class Friends(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    image = models.ImageField(upload_to='friends/', null=False)

    class Meta(object):
        ordering = ['my_order']
        verbose_name_plural = "friends"

    def __str__(self):
        return self.name


# https://goodcode.io/articles/django-singleton-models/
class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


class Bio(SingletonModel):
    text = models.TextField(blank=True)
    class Meta(object):
        verbose_name_plural = "bio"

class SelfPhoto(SingletonModel):
    image = models.ImageField(upload_to='me/', null=False)

    class Meta(object):
        verbose_name_plural = "Self Photo"
