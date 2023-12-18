from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=4096)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Category: {self.name}>"

    class Meta:
        verbose_name_plural = "categories"
