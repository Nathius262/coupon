# Generated by Django 4.1.3 on 2023-11-02 16:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pipay", "0019_alter_withdraw_bank_name_alter_withdraw_email_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="advertpost",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="advertpost",
            name="embed_link",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="taskpost",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="taskpost",
            name="embed_link",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="PayGig",
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
                ("embed_link", models.TextField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("task_completed", models.BooleanField(default=False)),
                (
                    "users",
                    models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
    ]
