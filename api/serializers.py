from scrapper.models import PlayerGoalScore

from rest_framework import serializers


class PlayerGoalScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerGoalScore
        fields = '__all__'
