from rest_framework import viewsets
from ...serializers.daily_quest_serializer import QuestSerializer
from ...models.daily_quest import Quest



class QuestsViewSet(viewsets.ModelViewSet):
    import datetime
    serializer_class = QuestSerializer

    from django.db.models import Q

    queryset = Quest.objects.filter(Q(permed=True)|Q(date=(datetime.datetime.utcnow()).replace(hour=0, minute=0, second=0, microsecond=0)))
