from rest_framework import serializers
from fight_covid19.maps.models import HealthEntry


class HealthEntrySerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(source="user.username")

    class Meta:
        model = HealthEntry
        fields = [
            "username",
            "fever",
            "cough",
            "difficult_breathing",
            "self_quarantine",
            "latitude",
            "longitude",
            "creation_timestamp",
        ]
