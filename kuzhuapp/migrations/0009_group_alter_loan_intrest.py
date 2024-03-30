# Generated by Django 5.0.3 on 2024-03-25 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kuzhuapp", "0008_alter_member_aadhaarnumber_alter_member_gaurdian_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Group",
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
                ("repay", models.IntegerField()),
                ("intrest", models.IntegerField()),
                ("savings", models.IntegerField()),
                ("sandha", models.IntegerField()),
                ("total", models.IntegerField()),
                ("mon", models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name="loan",
            name="intrest",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
