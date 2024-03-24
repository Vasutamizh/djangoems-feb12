# Generated by Django 5.0.2 on 2024-03-15 15:19

import django.db.models.deletion
import kuzhuapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuzhuapp', '0007_alter_member_aadhaarnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='Aadhaarnumber',
            field=models.IntegerField(default=0, validators=[kuzhuapp.models.maxlen]),
        ),
        migrations.AlterField(
            model_name='member',
            name='Gaurdian',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan', models.PositiveIntegerField()),
                ('intrest', models.CharField(blank=True, default=36, max_length=10, null=True)),
                ('mon', models.DateField(auto_now=True)),
                ('mem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kuzhuapp.member')),
            ],
        ),
    ]