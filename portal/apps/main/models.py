from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_participant = models.BooleanField(default=True)
    is_judge = models.BooleanField(default=False)
    is_team = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User: {self.username}>"
