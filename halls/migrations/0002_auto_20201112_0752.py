# Generated by Django 3.1.3 on 2020-11-12 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hall',
            old_name='User',
            new_name='user',
        ),
    ]
