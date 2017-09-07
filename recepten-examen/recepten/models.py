from __future__ import unicode_literals

from django.db import models


class Gerecht(models.Model):
    naam = models.CharField(max_length=100)
    ingredienten = models.CharField(max_length=100)
    bereidtijd = models.CharField(max_length=100)
    calorieen = models.CharField(max_length=100)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name