# Generated by Django 4.2.4 on 2023-08-15 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='Recipe',
        ),
    ]