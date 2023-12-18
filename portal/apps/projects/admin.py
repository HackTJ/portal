from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    autocomplete_fields = ("created_by", "last_modified_by", "location")
    date_hierarchy = "created_at"
    filter_horizontal = ("members", "categories")
    list_display = ("name", "location", "created_at", "modified_at")
    ordering = ("created_at",)
    save_as = True
    search_fields = ("name", "location")
