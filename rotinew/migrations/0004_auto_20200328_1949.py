# Generated by Django 3.0.1 on 2020-03-28 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rotinew', '0003_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rotii',
            old_name='userw',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='rotii',
            old_name='valuew',
            new_name='value',
        ),
    ]