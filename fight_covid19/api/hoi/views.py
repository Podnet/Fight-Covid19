import datetime

from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.db import transaction
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response

from fight_covid19.maps.helpers import get_hoi_stats
from fight_covid19.maps.models import HealthEntry
from .serializers import HealthEntrySerializer, HealthEntryFormSerializer

User = get_user_model()


class HealthEntryViewSet(viewsets.ModelViewSet):
    """API endpoints for the Health Entry Statistics"""

    queryset = HealthEntry.objects.all()
    serializer_class = HealthEntrySerializer

    def create(self, request, *args, **kwargs):
        entryform_serializer = HealthEntryFormSerializer(
            data=request.data, context={"request": request}
        )
        if entryform_serializer.is_valid():
            try:
                # Atomic transaction
                with transaction.atomic():
                    entry_form = entryform_serializer.save()
                    entry_form.creation_timestamp = datetime.datetime.now(
                        tz=timezone.utc
                    )
                    entry_form.save()
            except Exception as e:
                return Response({"error": str(e)})
            resp = HealthEntrySerializer(entry_form)
            return Response(resp.data)

            # If there are errors, return them
        else:
            errors = dict()
            entryform_serializer.is_valid()
            errors.update(dict(entryform_serializer.errors))
            return Response(errors)


class HealthStatisticsViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        hoi_stats = cache.get("hoi_stats", default=None)
        if not hoi_stats:
            hoi_stats = get_hoi_stats()
        return Response(hoi_stats)
