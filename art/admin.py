from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
# from .models import Artwork
from .models import Acrylic
from .models import Photograph
from .models import Watercolor

# Register your models here.

# admin.site.register(Artwork)


# @admin.register(Artwork)
@admin.register(Acrylic)
@admin.register(Photograph)
@admin.register(Watercolor)

class ArtworkAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
    # fieldsets = (
    #     (None, {
    #         'fields': ('name', 'image', 'category')
    #     }),
    #     ('Advanced options', {
    #         'classes': ('collapse',),
    #         'fields': ('description', 'price', 'size'),
    #     }),
    # )
    # list_display = ['name']
