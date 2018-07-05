# Generated by Django 2.0.7 on 2018-07-05 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerGoalScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('player_name', models.CharField(max_length=255)),
                ('goals_scored', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('minutes_played', models.IntegerField()),
                ('matches_played', models.IntegerField()),
                ('penalties_scored', models.IntegerField()),
                ('goals_left_foot', models.IntegerField()),
                ('goals_right_foot', models.IntegerField()),
                ('headed_goals', models.IntegerField()),
            ],
        ),
    ]
