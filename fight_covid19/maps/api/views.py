from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response

from fight_covid19.maps.helpers import get_stats
from fight_covid19.maps.models import HealthEntry
from .serializers import HealthEntrySerializer

User = get_user_model()


class HealthEntryViewSet(viewsets.ModelViewSet):
    """API endpoints for the Health Entry Statistics"""

    queryset = HealthEntry.objects.all()
    serializer_class = HealthEntrySerializer


class CoronaVirusCasesViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        data = dict()
        statewise = dict()  # To store total stats of the state
        last_updated = dict()
        total = dict()
        c = cache.get("stats", default=None)
        if not c:
            total, statewise, last_updated = get_stats()
        else:
            total, statewise, last_updated = c
        data["total"] = total
        data["statewise"] = statewise
        data["last_updated"] = last_updated
        return Response(data)


class HealthStatisticsViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        c = {}
        # Creating health statistics
        # HealthEntry.objects.filter(fever=True).count()
        # HealthEntry.objects.filter(cough=True).count()
        # HealthEntry.objects.filter(difficult_breathing=True).count()
        sick_people = HealthEntry.objects.filter(
            Q(fever=True) | Q(cough=True) | Q(difficult_breathing=True)
        )
        c["sickPeople"] = sick_people.count()
        c["totalPeople"] = (
            HealthEntry.objects.all().order_by("user").distinct("user_id").count()
        )

        return Response(c)
