from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class Team(models.Model):
    name = models.CharField("Name", max_length=150)
    mbtid = models.IntegerField()
    country = CountryField()
    
    def __str__(self):
        return self.name
    
    def get_nl_winner(self):
        return self.nl_winner.filter(league__level=1)