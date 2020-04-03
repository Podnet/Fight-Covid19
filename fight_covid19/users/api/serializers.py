from rest_framework import serializers

from fight_covid19.users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "name", "url","password"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
            "password": {"write_only": True , "min_length": 6}
        }
