from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import View
from django.views.generic.edit import FormView
from django.db.models import Count
from fight_covid19.maps import forms
from fight_covid19.maps.models import HealthEntry
from fight_covid19.maps.helpers import (
    get_covid19_stats,
    get_hoi_stats,
    get_map_markers,
    get_range_coords,
)


class HomePage(View):
    def get(self, request, *args, **kwargs):
        covid19_stats = cache.get("covid19_stats", default=None)
        hoi_stats = cache.get("hoi_stats", default=None)
        if not covid19_stats:
            covid19_stats = get_covid19_stats()
        if not hoi_stats:
            hoi_stats = get_hoi_stats()

        # else:
        #     total, statewise, last_updated = c
        return render(
            request,
            "pages/home.html",
            context={"covid19_stats": covid19_stats, "hoi_stats": hoi_stats},
        )


HomePageView = HomePage.as_view()


class HealthForm(LoginRequiredMixin, FormView):
    form_class = forms.HealthEntryForm
    template_name = "maps/health_form.html"
    success_url = reverse_lazy("maps:my_health")

    def form_valid(self, form):
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = self.request.user
            entry.save()

        return super().form_valid(form)


HealthFormView = HealthForm.as_view()


class MyHealth(LoginRequiredMixin, ListView):
    model = HealthEntry
    template_name = "maps/my_health.html"
    context_object_name = "entries"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by(
            "-creation_timestamp"
        )


MyHealthView = MyHealth.as_view()


class MapMarkers(View):
    def get(self, request, *args, **kwargs):
        points_list = cache.get("map_markers", default=None)
        if not points_list:
            points_list = get_map_markers()
        return JsonResponse(points_list, safe=False)


MapMarkersView = MapMarkers.as_view()


class NearCount(View):
    def get(self, request, *args, **kwargs):
        ranges = get_range_coords(
            request.GET["longitude"], request.GET["latitude"], request.GET["distance"]
        )

        total_count = (
            HealthEntry.objects.all()
            .filter(
                latitude__range=(ranges["min_lat"], ranges["max_lat"]),
                longitude__range=(ranges["min_lon"], ranges["max_lon"]),
            )
            .values("user_id")
            .annotate(total=Count("user_id"))
            .count()
        )

        return JsonResponse({"total": total_count})
