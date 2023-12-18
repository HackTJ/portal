from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=4096)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Category: {self.name}>"

    def get_absolute_url(self):
        return reverse("categories:detail", args=(self.id,))

    class Meta:
        verbose_name_plural = "categories"
