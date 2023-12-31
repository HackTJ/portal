# Generated by Django 5.0 on 2023-12-17 17:36

import portal.apps.locations.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "floor",
                    models.CharField(
                        choices=[("5", "5"), ("6", "6"), ("7", "7"), ("8", "8")], max_length=1
                    ),
                ),
                (
                    "room",
                    models.CharField(
                        blank=True,
                        max_length=5,
                        null=True,
                        validators=[portal.apps.locations.models.validate_room],
                    ),
                ),
                ("capacity", models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
        ),
    ]
