from django.urls import path
from fight_covid19.maps import views as map_views
from django.views.generic import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name="maps/maps.html"), name="home"),
    path("health_form/", map_views.HealthFormView, name="health_form"),
    path("map_markers/", map_views.MapMarkersView, name="map_markers"),
    path("my_health", map_views.MyHealthView, name="my_health"),
    path("patients_nearme", map_views.NearCount.as_view(), name="near_count"),
    path(
        "oneshot_health_entry",
        TemplateView.as_view(template_name="maps/one_shot_health_form.html"),
        name="oneshot_health_entry",
    ),
    path(
        "help_entry",
        TemplateView.as_view(template_name="maps/help_entry_form.html"),
        name="health_entry",
    ),
    path(
        "generate_unique_key",
        map_views.GenerateUniqueKey.as_view(),
        name="generate_unique_key",
    ),
    path(
        "oneshot_form_entry",
        map_views.OneShotFormEntry.as_view(),
        name="oneshot_form_entry",
    ),
]
