from django.urls import path
from fight_covid19.maps import views as map_views
from django.views.generic import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name="maps/maps.html"), name="home"),
    path(
        "wellness_entry_form/", map_views.WellnessEntryCreateView, name="wellness_entry"
    ),
    path("wellness_entries", map_views.WellnessEntryListView, name="wellness_entries"),
]
