from django.contrib import admin
from .models import CurrentShow
from .models import PreviousVenue

# Register your models here.


admin.site.register(CurrentShow)
admin.site.register(PreviousVenue)
