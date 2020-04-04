from rest_framework import serializers

from fight_covid19.maps.models import HealthEntry


class HealthEntryFormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HealthEntry
        fields = [
            "user_id",
            "fever",
            "cough",
            "difficult_breathing",
            "self_quarantine",
            "latitude",
            "longitude",
        ]


class HealthEntrySerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.CharField(source="user.username")

    class Meta:
        model = HealthEntry
        fields = [
            "id",
            "user",
            "fever",
            "cough",
            "difficult_breathing",
            "self_quarantine",
            "latitude",
            "longitude",
            "creation_timestamp",
        ]
