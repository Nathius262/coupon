# Generated by Django 4.1.3 on 2023-05-24 00:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pipay', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('USD', '$'), ('Naira', 'N'), ('Pakistani Rupee', 'PKR'), ('Ghanaian Cedis', 'GHS')], default='N', editable=False, max_length=50)),
                ('affilate', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=12)),
                ('task', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=12)),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
