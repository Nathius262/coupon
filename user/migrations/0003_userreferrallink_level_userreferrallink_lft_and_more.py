# Generated by Django 4.1.3 on 2023-07-23 18:19

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreferrallink',
            name='level',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userreferrallink',
            name='lft',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userreferrallink',
            name='parent',
            field=mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_referral_parent', to='user.userreferrallink'),
        ),
        migrations.AddField(
            model_name='userreferrallink',
            name='rght',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userreferrallink',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
            preserve_default=False,
        ),
    ]
