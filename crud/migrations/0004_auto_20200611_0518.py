# Generated by Django 3.0.7 on 2020-06-10 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20200610_2307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Fullname',
            new_name='fullname',
        ),
    ]
