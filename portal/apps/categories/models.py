from django.db import models
from django.urls import reverse
from rules.contrib.models import RulesModel

from ..main.rules import is_admin


class Category(RulesModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=4096)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Category: {self.name}>"

    def get_absolute_url(self):
        return reverse("categories:detail", args=(self.id,))

    class Meta:
        rules_permissions = {
            "list": is_admin,
            "add": is_admin,
            "view": is_admin,
            "change": is_admin,
            "delete": is_admin,
        }
        verbose_name_plural = "categories"
