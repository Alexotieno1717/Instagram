# Generated by Django 3.1.2 on 2020-10-19 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_auto_20201019_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='images',
        ),
    ]
