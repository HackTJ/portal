from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    date_hierarchy = "date_joined"
    list_display = ("username", "email", "is_participant", "is_judge", "is_team")
    list_filter = ("is_participant", "is_judge", "is_team")
    search_fields = ("username", "email")
    ordering = ("username",)


