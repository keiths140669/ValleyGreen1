# Generated by Django 4.0.3 on 2022-09-17 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, null=True, verbose_name='Last Name')),
            ],
        ),
        migrations.CreateModel(
            name='TeamName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100, null=True, verbose_name='Team Name')),
                ('age_group', models.CharField(choices=[('U7', 'U7'), ('U8', 'U8'), ('U9', 'U9'), ('U10', 'U10'), ('U11', 'U11'), ('U12', 'U12'), ('U13', 'U13'), ('U14', 'U14'), ('U15', 'U15'), ('U16', 'U16')], max_length=3, null=True)),
                ('venue', models.CharField(max_length=120, null=True, verbose_name='Venue')),
                ('address', models.CharField(max_length=200, null=True, verbose_name='Address')),
                ('contact', models.CharField(max_length=60, null=True, verbose_name='Contact Name')),
                ('contact_mob', models.CharField(max_length=15, null=True, verbose_name='Contact Mobile No')),
                ('contact_email', models.EmailField(max_length=200, null=True, verbose_name='Email')),
                ('map_link', models.URLField(max_length=300, null=True, verbose_name='Map Address Link')),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat_date', models.DateTimeField(verbose_name='Stat Date')),
                ('stat_goal_assists', models.IntegerField(null=True, verbose_name='Goal Assists')),
                ('stat_goals_scored', models.IntegerField(null=True, verbose_name='Goals Scored')),
                ('age_group', models.CharField(choices=[('U7', 'U7'), ('U8', 'U8'), ('U9', 'U9'), ('U10', 'U10'), ('U11', 'U11'), ('U12', 'U12'), ('U13', 'U13'), ('U14', 'U14'), ('U15', 'U15'), ('U16', 'U16')], max_length=3, null=True)),
                ('player_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='football.player')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='football.teamname')),
            ],
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixture_date', models.DateTimeField(verbose_name='Fixture Date')),
                ('age_group', models.CharField(choices=[('U7', 'U7'), ('U8', 'U8'), ('U9', 'U9'), ('U10', 'U10'), ('U11', 'U11'), ('U12', 'U12'), ('U13', 'U13'), ('U14', 'U14'), ('U15', 'U15'), ('U16', 'U16')], max_length=3, null=True)),
                ('half_time', models.CharField(blank=True, max_length=10, verbose_name='Half Time')),
                ('full_time', models.CharField(blank=True, max_length=10, verbose_name='Full Time')),
                ('player_of_the_match', models.CharField(blank=True, max_length=80, verbose_name='Player Of The Match')),
                ('goal_assists', models.IntegerField(null=True, verbose_name='Goal Assists')),
                ('goals_scored', models.IntegerField(null=True, verbose_name='Goals Scored')),
                ('comments', models.CharField(blank=True, max_length=280, verbose_name='Comments')),
                ('away_team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='football.teamname')),
                ('home_team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='football.teamname')),
                ('playing', models.ManyToManyField(blank=True, to='football.player')),
            ],
        ),
    ]
