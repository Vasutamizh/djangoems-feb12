# Generated by Django 5.0.2 on 2024-03-10 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuzhuapp', '0003_alter_member_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emi',
            name='loan',
        ),
        migrations.RenameField(
            model_name='emi',
            old_name='member',
            new_name='mem',
        ),
        migrations.AddField(
            model_name='member',
            name='Loanamount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='emis',
            field=models.ManyToManyField(to='kuzhuapp.emi'),
        ),
        migrations.DeleteModel(
            name='Loan',
        ),
    ]
