from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    ordering = ("name",)
    save_as = True
    search_fields = ("name", "description")
