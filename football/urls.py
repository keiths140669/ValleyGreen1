from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('fixture_U10', views.fixture_U10, name="fixture-U10"),
    path('fixture_U11', views.fixture_U11, name='fixture-U11'),
    path('stats_U9', views.stats_players_U9, name='player-stats-U9'),
    path('stats_U10', views.stats_players_U10, name='player-stats-U10'),
    path('goals_scored_U11', views.goals_scored_U11, name='goals-scored-U11'),
    path('team_name_U10', views.team_name_U10, name='team-name-U10'),
    path('team_name_U9', views.team_name_U9, name='team-name-U9'),
    path('team_name_U11', views.team_name_U11, name='team-name-U11'),
    path('add_team', views.get_team_name_form, name='get_team_name'),
    path('update_team_name/<tm_id>', views.update_team_name, name='update-team-name'),
]