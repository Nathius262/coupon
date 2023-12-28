# Generated by Django 4.1.3 on 2023-10-21 11:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pipay", "0014_taskpost_users"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdvertPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("post_link", models.URLField(blank=True)),
                ("task_completed", models.BooleanField(default=False)),
                (
                    "users",
                    models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
    ]
