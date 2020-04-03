from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from fight_covid19.maps.api.views import HealthEntryViewSet
from fight_covid19.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("healthentry", HealthEntryViewSet)

app_name = "api"
urlpatterns = router.urls
