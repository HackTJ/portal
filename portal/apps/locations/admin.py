from django.contrib import admin

from portal.apps.locations.models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "floor", "room", "capacity")
    search_fields = ("name", "room")
    ordering = (
        "floor",
        "room",
    )
    list_filter = ("floor",)
