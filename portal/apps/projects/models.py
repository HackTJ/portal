from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from rules.contrib.models import RulesModel

from .rules import no_other_projects, is_project_member
from ..categories.models import Category
from ..locations.models import Location
from ..main.models import User
from ..main.rules import is_admin


class Project(RulesModel):
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
        return self.name

    def __repr__(self):
        return f"<Project: {self.name}>"

    def get_absolute_url(self):
        return reverse("projects:detail", args=(self.id,))

    class Meta:
        default_related_name = "projects"
        get_latest_by = "created_at"
        rules_permissions = {
            "list": is_admin,
            "add": is_admin | no_other_projects,
            "view": is_admin | is_project_member,
            "change": is_admin | is_project_member,
            "delete": is_admin | is_project_member,
            "leave": is_project_member,
        }
