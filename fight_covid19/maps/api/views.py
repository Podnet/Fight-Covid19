import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView

from fight_covid19.maps.models import HealthEntry
from .serializers import HealthEntrySerializer

User = get_user_model()


class HealthEntryViewSet(viewsets.ModelViewSet):
    """API endpoints for the Health Entry Statistics"""

    queryset = HealthEntry.objects.all()
    serializer_class = HealthEntrySerializer


class CoronaVirusCasesViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        c = {
            "cases": "N/A",
            "activeCases": "N/A",
            "todayCases": "N/A",
            "deaths": "N/A",
            "todayDeaths": "N/A",
            "recovered": "N/A",
            "critical": "N/A",
        }

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

        # Fetching data from API
        r = requests.get(settings.COVID19_STATS_API)
        if r.status_code == 200:
            data = r.json()
            india_stats = list(filter(lambda x: x["country"] == "India", data))
            c["cases"] = india_stats[0]["cases"]
            c["todayCases"] = india_stats[0]["todayCases"]
            c["deaths"] = india_stats[0]["deaths"]
            c["todayDeaths"] = india_stats[0]["todayDeaths"]
            c["recovered"] = india_stats[0]["recovered"]
            c["active"] = india_stats[0]["active"]
            c["critical"] = india_stats[0]["critical"]

        return Response(c)


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
