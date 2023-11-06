from django.db import models

class Location(models.Model):
    city = models.CharField(max_length=10, blank=False, null=False)
    gu = models.CharField(max_length=20, blank=False, null=False)
    nx = models.PositiveIntegerField(blank=False, null=False)
    my = models.PositiveIntegerField(blank=False, null=False)