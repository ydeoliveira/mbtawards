from django.urls import path
from .views import TeamAwards

urlpatterns = [
    path('team/<int:team_id>',TeamAwards.as_view(),name='teamawards'),
]