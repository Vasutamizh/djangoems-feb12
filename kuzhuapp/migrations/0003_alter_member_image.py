# Generated by Django 5.0.2 on 2024-03-09 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuzhuapp', '0002_member_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='Image',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
    ]