from django.contrib import admin
from .models import TeamName
from .models import Fixture
from .models import Player
from .models import Stat


@admin.register(TeamName)
class TeamNameAdmin(admin.ModelAdmin):
	list_display = ('team_name', 'age_group')
	ordering = ('team_name',)

@admin.register(Stat)
class StatsAdmin(admin.ModelAdmin):
	list_display = ('stat_date', 'player_name', 'stat_goal_assists', 'stat_goals_scored', 'team', 'age_group')
	ordering = ('-stat_date',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name')
	ordering = ('first_name',)

@admin.register(Fixture)
class FixturesAdmin(admin.ModelAdmin):
	list_display = ('fixture_date', 'home_team', 'away_team', 'age_group')
	ordering = ('-fixture_date',)
