import requests
from django.conf import settings
from django.core.cache import cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import View
from django.views.generic.edit import FormView
from django.http import JsonResponse
from django.db.models import Q
from fight_covid19.maps import forms
from fight_covid19.maps.models import HealthEntry
from fight_covid19.maps.helpers import get_stats, get_map_markers


class HomePage(View):
    def get(self, request, *args, **kwargs):
        c = cache.get("stats", default=None)
        if not c:
            c = get_stats()
        return render(request, "pages/home.html", context=c)


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
