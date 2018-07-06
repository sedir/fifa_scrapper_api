from api.serializers import PlayerGoalScoreSerializer
from scrapper.models import PlayerGoalScore

from rest_framework import viewsets


class PlayerGoalScoreViewSet(viewsets.ModelViewSet):
    queryset = PlayerGoalScore.objects.all()
    serializer_class = PlayerGoalScoreSerializer
