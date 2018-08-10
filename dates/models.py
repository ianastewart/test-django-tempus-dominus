from django.db import models

# Create your models here.

class DateTest(models.Model):
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    datetime = models.DateTimeField(null=True)
    comment = models.CharField(max_length=20, null=True, blank=True)