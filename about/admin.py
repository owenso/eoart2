from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Bio
from .models import Friends
# Register your models here.


@admin.register(Bio)
@admin.register(Friends)

class AboutAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass