# Generated by Django 4.2.4 on 2023-09-01 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0005_remove_rating_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='UserId',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
