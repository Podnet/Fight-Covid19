from rest_framework import serializers

from fight_covid19.users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "url",
            "username",
            "password",
            "first_name",
            "last_name",
            "name",
            "email",
            "is_active",
            "is_staff",
            "is_superuser",
            "password",
            "groups",
            "date_joined",
            "last_login",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
            "password": {"write_only": True, "min_length": 6},
        }
