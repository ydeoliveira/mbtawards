from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField


REGIONS = (("Adriatic", "Adriatic"),
           ("Asia", "Asia"),
           ("Baltic", "Baltic"),
           ("Central Europe", "Central Europe"),
           ("Eastern Europe", "Eastern Europe"),
           ("Mediterranean", "Mediterranean"),
           ("North America", "North America"),
           ("Rest of the World", "Rest of the World"),
           ("Scandinavia", "Scandinavia"),
           ("South America", "South America"),
           ("Western Europe", "Western Europe"),
           )

# Create your models here.
class NationalLeague(models.Model):
    country = CountryField()
    level = models.PositiveIntegerField("Level", validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ])
    group = models.IntegerField()
    verbose_name = models.CharField("Name", blank=True, null=True, max_length=150)
    #ajouter contrainte unique together (country level, group)
    def clean(self):
        if self.group > int(pow(2, self.level)/2):
            raise ValidationError("The number of groups can't exceed {0} for level {1}".format(int(pow(2, self.level)/2), self.level))
        if self.level != 1:
            self.verbose_name = ''
    
    def __str__(self):
        if self.verbose_name :
            return "[{0}] {1}".format(self.country, self.verbose_name)
        else :
            return "[{0}] {1}.{2}".format(self.country, self.level, self.group)
    
class RegionalLeague(models.Model):
    region = models.CharField("Region", max_length=50, choices=REGIONS)
    level = models.PositiveIntegerField("Level", validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    #ajouter contrainte unique together (region, level)
    def __str__(self):
        return "{0} Regional League level {1}".format(self.region, self.level)
        