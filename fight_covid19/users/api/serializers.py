from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


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
        read_only_fields = ("is_active", "is_staff", "is_superuser")
        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
            "password": {"write_only": True, "min_length": 6},
        }
