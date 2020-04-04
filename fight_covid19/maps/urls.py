from django.urls import path
from fight_covid19.maps import views as map_views
from django.views.generic import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name="maps/maps.html"), name="home"),
    path("health_form/", map_views.HealthFormView, name="health_form"),
    path("map_markers/", map_views.MapMarkersView, name="map_markers"),
    path("my_health", map_views.MyHealthView, name="my_health"),
    path("count", map_views.NearCount.as_view(), name="near_count"),
]
