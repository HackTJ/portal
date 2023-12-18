from django.core.exceptions import ValidationError
from django.db import models

from ..categories.models import Category
from ..locations.models import Location
from ..main.models import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=4096)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    members = models.ManyToManyField(User)
    created_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name="created_projects"
    )
    last_modified_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="last_modified_projects",
    )

    categories = models.ManyToManyField(Category)

    location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.SET_NULL)
    location_description = models.CharField(max_length=1024, null=True, blank=True)

    def clean(self):
        if not self.location and not self.location_description:
            raise ValidationError("Must set either location or location description.")

    def __str__(self):
        if self.location:
            return f"{self.name} ({self.location})"
        return self.name

    def __repr__(self):
        return f"<Project: {self.name}>"

    class Meta:
        default_related_name = "projects"
        get_latest_by = "created_at"
