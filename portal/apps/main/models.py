from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_participant = models.BooleanField(default=True)
    is_judge = models.BooleanField(default=False)
    is_team = models.BooleanField(default=False)

    @property
    def is_admin(self):
        return self.is_superuser or self.is_team

    def has_module_perms(self, app_label):
        if self.is_admin:
            return True
        return super().has_module_perms(app_label)

    def has_perm(self, perm, obj=None):
        if self.is_admin:
            return True
        return super().has_perm(perm, obj)

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User: {self.username}>"
