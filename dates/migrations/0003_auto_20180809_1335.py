# Generated by Django 2.0.8 on 2018-08-09 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dates', '0002_datetest_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datetest',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='datetest',
            name='datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='datetest',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
