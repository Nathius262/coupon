# Generated by Django 4.1.3 on 2023-05-24 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipay', '0002_usersbalance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersbalance',
            name='currency',
            field=models.CharField(choices=[('USD', '$'), ('Naira', 'N'), ('Pakistani Rupee', 'PKR'), ('Ghanaian Cedis', 'GHS')], default='Naira', editable=False, max_length=50),
        ),
    ]
