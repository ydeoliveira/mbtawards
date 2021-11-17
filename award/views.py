from django.shortcuts import render
from django.views import View

from team.models import Team
# Create your views here.
class TeamAwards(View):
    template = "awards/team.html"
    
    def get(self, request, team_id):
        team = Team.objects.get(id = team_id)
        return render(request, self.template, {'team':team})