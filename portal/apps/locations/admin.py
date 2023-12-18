from django.contrib import admin

from .models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "floor", "room", "capacity")
    list_filter = ("floor",)
    ordering = ("floor", "room")
    save_as = True
    search_fields = ("name", "room")
