# Generated by Django 2.0.8 on 2018-08-09 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datetest',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 9, 12, 39, 20, 652244)),
            preserve_default=False,
        ),
    ]
