from django.core.exceptions import ValidationError
from django.db import models
from rules.contrib.models import RulesModel

from ..main.rules import admin_only


def validate_room(value):
    # Four numbers and an optional letter (e.g. 5214, 5217A)
    if not value:
        return

    if len(value) < 4 or len(value) > 5:
        raise ValidationError("Room number must be 4-5 characters long.")

    if not value[:4].isdigit():
        raise ValidationError("First four characters of room number must be digits.")

    if len(value) == 5 and not value[4].isalpha():
        raise ValidationError("Fifth character of room number must be a letter.")


class Location(RulesModel):
    name = models.CharField(max_length=255, null=True, blank=True)

    FLOORS = ((x, x) for x in ("5", "6", "7", "8"))
    floor = models.CharField(max_length=1, choices=FLOORS)

    room = models.CharField(max_length=5, null=True, blank=True, validators=[validate_room])

    capacity = models.PositiveSmallIntegerField(null=True, blank=True)

    def clean(self):
        if self.room and self.room[0] != self.floor:
            raise ValidationError("Room number must start with the floor number.")

    def __str__(self):
        if self.name and self.room:
            return f"{self.room} {self.name}"
        elif self.name:
            return self.name
        elif self.room:
            return self.room
        else:
            return f"Location {self.id}"

    def __repr__(self):
        return f"<Location: {self.__str__()}>"

    class Meta:
        rules_permissions = {
            "list": admin_only,
            "add": admin_only,
            "view": admin_only,
            "change": admin_only,
            "delete": admin_only,
        }
