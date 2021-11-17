from django.db import models

from league.models import NationalLeague, RegionalLeague
from team.models import Team
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.
class NationalLeagueAward(models.Model):
    season = models.IntegerField()
    league = models.ForeignKey(NationalLeague, on_delete=CASCADE)
    first = models.ForeignKey(Team, related_name="nl_winner", null=True, on_delete=SET_NULL)
    second = models.ForeignKey(Team, related_name="nl_second", null=True, on_delete=SET_NULL)
    third = models.ForeignKey(Team, related_name="nl_third", null=True, on_delete=SET_NULL)
    
    def __str__(self):
        return "{0} season {1} winner : {2}".format(self.league, self.season, self.first)

class RegionalLeague(models.Model):
    season = models.IntegerField()
    league = models.ForeignKey(RegionalLeague, on_delete=CASCADE)
    winner = models.ForeignKey(Team, related_name="rl_winner", null=True, on_delete=SET_NULL)
    runnerup = models.ForeignKey(Team, related_name="rl_runner_up", null=True, on_delete=SET_NULL)
    
    def __str__(self):
        return "{0} season {1} winner : {2}".format(self.league, self.season, self.winner)
    
class ChampionsLeague(models.Model):
    season = models.IntegerField()
    winner = models.ForeignKey(Team, related_name="cl_winner", null=True, on_delete=SET_NULL)
    runnerup = models.ForeignKey(Team, related_name="cl_runner_up", null=True, on_delete=SET_NULL)
    def __str__(self):
        return "Champions League season {0} winner : {1}".format(self.season, self.winner)
