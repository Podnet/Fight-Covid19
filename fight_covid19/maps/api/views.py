from django.contrib.auth import get_user_model
from rest_framework import viewsets

from fight_covid19.maps.models import HealthEntry
from .serializers import HealthEntrySerializer

User = get_user_model()


class HealthEntryViewSet(viewsets.ModelViewSet):
    """API endpoints for the Health Entry Statistics"""

    queryset = HealthEntry.objects.all()
    serializer_class = HealthEntrySerializer
