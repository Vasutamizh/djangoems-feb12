# Generated by Django 5.0.2 on 2024-03-12 13:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuzhuapp', '0005_alter_member_aadhaarnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='Aadhaarnumber',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(12)]),
        ),
    ]
