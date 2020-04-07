from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from fight_covid19.api.coronacases.views import CoronaVirusCasesViewSet
from fight_covid19.api.hoi.views import HealthEntryViewSet, HealthStatisticsViewSet
from fight_covid19.api.news.views import NewsViewSet
from fight_covid19.api.users.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("healthentry", HealthEntryViewSet)
router.register("healthstat", HealthStatisticsViewSet, "healthstat")
router.register("coronacases", CoronaVirusCasesViewSet, "coronacases")
router.register("news", NewsViewSet, "news")

app_name = "api"
urlpatterns = router.urls
