from django.core.exceptions import ValidationError
from django.db import models


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


class Location(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    FLOORS = ((x, x) for x in ("5", "6", "7", "8"))
    floor = models.CharField(max_length=1, choices=FLOORS)

    room = models.CharField(max_length=5, null=True, blank=True, validators=[validate_room])

    capacity = models.PositiveSmallIntegerField(null=True, blank=True)

    def clean(self):
        if self.room and self.room[0] != self.floor:
            raise ValidationError("Room number must start with the floor number.")

    def __str__(self):
        value = self.room if self.room else f"F-{self.floor}"
        if self.name:
            value += f" ({self.name})"
        if self.capacity:
            value += f" [{self.capacity}]"
        return value

    def __repr__(self):
        return f"<Location: {self.__str__()}>"
