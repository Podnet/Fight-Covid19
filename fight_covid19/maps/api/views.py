from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.db.models import Q
from django.db import transaction
from rest_framework import viewsets
from rest_framework.response import Response
import datetime
from django.utils import timezone
from fight_covid19.maps.helpers import get_stats
from fight_covid19.maps.models import HealthEntry
from .serializers import HealthEntrySerializer, HealthEntryFormSerializer

User = get_user_model()


class HealthEntryViewSet(viewsets.ModelViewSet):
    """API endpoints for the Health Entry Statistics"""

    queryset = HealthEntry.objects.all()
    serializer_class = HealthEntrySerializer

    def create(self, request, format=None, *args, **kwargs):
        entryform_serializer = HealthEntryFormSerializer(
            data=request.data, context={"request": request}
        )
        if entryform_serializer.is_valid():
            try:
                # Atomic transaction
                with transaction.atomic():
                    entry_form = entryform_serializer.save()
                    entry_form.user = User.objects.get(pk=request.data["user_id"])
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
            HealthEntryFormSerializer.is_valid()
            errors.update(dict(HealthEntryFormSerializer.errors))
            return Response(errors)


class CoronaVirusCasesViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        data = dict()
        statewise = dict()  # To store total stats of the state
        last_updated = dict()
        total = dict()
        c = cache.get("stats", default=None)
        if not c:
            c = get_stats()
        data["total"] = c[0]
        data["statewise"] = c[1:-1]
        data["last_updated"] = c[-1]
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
