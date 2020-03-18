from django.views.generic.edit import CreateView
from django.views.generic import View
from fight_covid19.maps.models import WellnessEntry
from django.shortcuts import render
from django.conf import settings
import requests


class HomePage(View):
    def get(self, request, *args, **kwargs):
        print("hello")
        c = {
            "cases": "N/A",
            "todayCases": "N/A",
            "deaths": "N/A",
            "todayDeaths": "N/A",
            "recovered": "N/A",
            "critical": "N/A",
        }
        r = requests.get(settings.COVID19_STATS_API)
        if r.status_code == 200:
            data = r.json()
            india_stats = list(filter(lambda x: x["country"] == "India", data))
            c = india_stats[0]
            print("Donbe")

        return render(request, "pages/home.html", context=c)


HomePageView = HomePage.as_view()


class WellnessEntryCreate(CreateView):
    model = WellnessEntry
    fields = "__all__"


WellnessEntryCreateView = WellnessEntryCreate.as_view()
