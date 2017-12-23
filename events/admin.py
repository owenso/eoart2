from django.contrib import admin
from .models import CurrentShow
from .models import PreviousVenue

# Register your models here.



@admin.register(CurrentShow)
class CurrentShowAdmin(admin.ModelAdmin):
    fields = ('venue_name', 'address', 'url', ('start_date',
                                               'start_time'), ('end_date', 'end_time'), 'show_image')
    list_display = ('venue_name', 'address', 'start_date', 'end_date')

@admin.register(PreviousVenue)
class PreviousVenueAdmin(admin.ModelAdmin):
    pass
