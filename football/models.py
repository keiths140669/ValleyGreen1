from django.db import models


class TeamName(models.Model):
	STATUS = [
		('U7', 'U7'),
		('U8', 'U8'),
		('U9', 'U9'),
		('U10', 'U10'),
		('U11', 'U11'),
		('U12', 'U12'),
		('U13', 'U13'),
		('U14', 'U14'),
		('U15', 'U15'),
		('U16', 'U16'),
		]
	team_name = models.CharField('Team Name', max_length=100, null=True)
	age_group = models.CharField(choices=STATUS, max_length=3, null=True)
	venue = models.CharField('Venue', max_length=120, null=True)
	address = models.CharField('Address', max_length=200, null=True)
	contact = models.CharField('Contact Name', max_length=60, null=True)
	contact_mob = models.CharField('Contact Mobile No', max_length=15, null=True)
	contact_email = models.EmailField('Email', max_length=200, null=True)
	map_link = models.URLField('Map Address Link', max_length=300, null=True)

	def __str__(self):
		return self.team_name + " " + self.age_group

class Player(models.Model):
	first_name = models.CharField('First Name', max_length=100, null=True)
	last_name = models.CharField('Last Name', max_length=100, null=True)

	def __str__(self):
		return self.first_name + " " + self.last_name

class Stat(models.Model):
	STATUS = [
		('U7', 'U7'),
		('U8', 'U8'),
		('U9', 'U9'),
		('U10', 'U10'),
		('U11', 'U11'),
		('U12', 'U12'),
		('U13', 'U13'),
		('U14', 'U14'),
		('U15', 'U15'),
		('U16', 'U16'),
		]
	stat_date = models.DateTimeField('Stat Date')
	player_name = models.ForeignKey(Player, null=True, on_delete=models.CASCADE)
	stat_goal_assists = models.IntegerField('Goal Assists', null=True)
	stat_goals_scored = models.IntegerField('Goals Scored', null=True)
	team = models.ForeignKey(TeamName, null=True, on_delete=models.CASCADE)
	age_group = models.CharField(choices=STATUS, max_length=3, null=True)
	

	def __str__(self):
		return '{}{}'.format(self.stat_date, self.player_name)

class Fixture(models.Model):
	STATUS = [
		('U7', 'U7'),
		('U8', 'U8'),
		('U9', 'U9'),
		('U10', 'U10'),
		('U11', 'U11'),
		('U12', 'U12'),
		('U13', 'U13'),
		('U14', 'U14'),
		('U15', 'U15'),
		('U16', 'U16'),
		]
	fixture_date = models.DateTimeField('Fixture Date')
	age_group = models.CharField(choices=STATUS, max_length=3, null=True)
	home_team = models.ForeignKey(TeamName, null=True, related_name='home_team', on_delete=models.CASCADE)
	away_team = models.ForeignKey(TeamName, null=True, related_name='away_team', on_delete=models.CASCADE)
	half_time = models.CharField('Half Time', max_length=10, blank=True)
	full_time = models.CharField('Full Time', max_length=10, blank=True)
	player_of_the_match = models.CharField('Player Of The Match', max_length=80, blank=True)
	goal_assists = models.IntegerField('Goal Assists', null=True)
	goals_scored = models.IntegerField('Goals Scored', null=True)
	comments = models.CharField('Comments', max_length=280, blank=True)
	playing = models.ManyToManyField(Player, blank=True)

	def __str__(self):
		return str(self.fixture_date)


