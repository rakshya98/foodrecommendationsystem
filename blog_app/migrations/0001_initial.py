# Generated by Django 4.2.4 on 2023-09-21 00:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=5000)),
                ('pub_date', models.DateField(default=datetime.date.today)),
                ('thumbnail', models.URLField()),
            ],
        ),
    ]
