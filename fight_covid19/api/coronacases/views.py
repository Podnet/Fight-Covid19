from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.response import Response

from fight_covid19.maps.helpers import get_covid19_stats


class CoronaVirusCasesViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        covid19_stats = cache.get("covid19_stats", default=None)
        if not covid19_stats:
            covid19_stats = get_covid19_stats()
        return Response(covid19_stats)
