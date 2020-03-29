import requests
from django.conf import settings
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


class HomePage(View):
    def get(self, request, *args, **kwargs):
        c = {
            "cases": "N/A",
            "activeCases": "N/A",
            "todayCases": "N/A",
            "deaths": "N/A",
            "todayDeaths": "N/A",
            "recovered": "N/A",
            "critical": "N/A",
        }

        # Creating health statistics
        # HealthEntry.objects.filter(fever=True).count()
        # HealthEntry.objects.filter(cough=True).count()
        # HealthEntry.objects.filter(difficult_breathing=True).count()
        sick_people = HealthEntry.objects.filter(
            Q(fever=True) | Q(cough=True) | Q(difficult_breathing=True)
        )
        c["sickPeople"] = sick_people.count()
        c["totalPeople"] = (
            HealthEntry.objects.all().order_by("user").distinct("user_id").count()
        )

        # Fetching data from API
        r = requests.get(settings.COVID19_STATS_API)
        if r.status_code == 200:
            data = r.json()
            india_stats = list(filter(lambda x: x["country"] == "India", data))
            c["cases"] = india_stats[0]["cases"]
            c["todayCases"] = india_stats[0]["todayCases"]
            c["deaths"] = india_stats[0]["deaths"]
            c["todayDeaths"] = india_stats[0]["todayDeaths"]
            c["recovered"] = india_stats[0]["recovered"]
            c["active"] = india_stats[0]["active"]
            c["critical"] = india_stats[0]["critical"]

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
        points = (
            HealthEntry.objects.all()
            .order_by("user", "-creation_timestamp")
            .distinct("user")
            .values("user_id", "latitude", "longitude")
        )
        return JsonResponse(list(points), safe=False)


MapMarkersView = MapMarkers.as_view()
