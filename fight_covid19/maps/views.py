from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import View
from django.views.generic.edit import FormView
from django.db.models import Count
from geopy.geocoders import Nominatim

from fight_covid19.maps import forms
from fight_covid19.maps.helpers import (
    get_covid19_stats,
    get_hoi_stats,
    get_map_markers,
    get_range_coords,
)
from fight_covid19.maps.models import HealthEntry
from fight_covid19.maps.models import HelpEntry
from fight_covid19.maps.models import KeyValuePair


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
            float(request.GET.get("latitude")),
            float(request.GET.get("longitude")),
            float(request.GET.get("distance", 5)),
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

        """TO get the location of the people by coordinates"""
        geolocator = Nominatim(user_agent="Health of India")
        location = geolocator.reverse(
            "{0}, {1}".format(request.GET.get("latitude"), request.GET.get("longitude"))
        )
        address = location.address

        data = dict()
        data["address"] = address
        data["total"] = total_count
        return JsonResponse(data)


class GenerateUniqueKey(View):
    def get(self, request, *args, **kwargs):
        try:
            counter = KeyValuePair.objects.get(name="unique_key_counter")
        except KeyValuePair.DoesNotExist:
            counter = KeyValuePair.objects.create(name="unique_key_counter", value="1")

        unique_id = counter.value

        # Updating values
        counter.value = str(int(counter.value) + 1)
        counter.save()

        return JsonResponse({"id": unique_id})


class OneShotFormEntry(View):
    def post(self, request, *args, **kwargs):
        raw_data = request.body.decode("utf-8")
        form_data = json.loads(raw_data)
        HealthEntry.objects.create(
            age=form_data["age"],
            gender=form_data["gender"],
            fever=form_data["fever"],
            cough=form_data["cough"],
            difficult_breathing=form_data["difficult_breathing"],
            self_quarantine=form_data["quarantine"],
            latitude=form_data["latitude"],
            longitude=form_data["longitude"],
            unique_id=form_data["unique_id"],
        )
        return JsonResponse({"status": "success"})


class HelpEntryForm(View):
    def post(self, request, *args, **kwargs):
        raw_data = request.body.decode("utf-8")
        form_data = json.loads(raw_data)
        HelpEntry.objects.create(
            fullname=form_data["fullname"],
            phone_number=form_data["phone_number"],
            help_type=form_data["help_type"],
            address=form_data["address"],
            description=form_data["description"],
            latitude=form_data["latitude"],
            longitude=form_data["longitude"],
        )
        return JsonResponse({"status": "success"})
