# Generated by Django 4.1.3 on 2023-05-31 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipay', '0007_alter_usersbalance_currency_alter_usersbalance_user'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='usersbalance',
            name='pipay_usersbalance_currency_valid',
        ),
        migrations.AlterField(
            model_name='usersbalance',
            name='currency',
            field=models.CharField(choices=[('$', 'Dollar'), ('USD', 'Usd'), ('N', 'Naira'), ('PKR', 'Pakistani Rupee'), ('INR', 'Indian Rupee'), ('GHS', 'Ghanaian Cedis'), ('PHP', 'Phillippine Peso'), ('ZAR', 'South African Rand')], default='N', editable=False, max_length=50),
        ),
        migrations.AddConstraint(
            model_name='usersbalance',
            constraint=models.CheckConstraint(check=models.Q(('currency__in', ['$', 'USD', 'N', 'PKR', 'INR', 'GHS', 'PHP', 'ZAR'])), name='pipay_usersbalance_currency_valid'),
        ),
    ]
