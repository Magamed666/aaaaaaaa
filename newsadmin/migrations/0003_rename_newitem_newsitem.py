# Generated by Django 4.1 on 2022-08-11 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsadmin', '0002_rename_userprofile_newitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewItem',
            new_name='NewsItem',
        ),
    ]