from django.contrib import admin
from django.contrib.auth.models import Group

from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in MenuItem._meta.get_fields() if field.name != "id"
    ]
    search_fields = ("name", "price")
    list_display_links = list_display


admin.site.unregister(Group)
