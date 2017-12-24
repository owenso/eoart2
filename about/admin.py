from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Bio
from .models import Friends
from .models import SelfPhoto

# Register your models here.

@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    pass

@admin.register(Friends)
class FriendsAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

@admin.register(SelfPhoto)
class SelfPhotoAdmin(admin.ModelAdmin):
    pass