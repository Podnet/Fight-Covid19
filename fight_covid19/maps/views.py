import requests
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import FormView

from fight_covid19.maps import forms


class HomePage(View):
    def get(self, request, *args, **kwargs):
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

        return render(request, "pages/home.html", context=c)


HomePageView = HomePage.as_view()


class WellnessEntryCreate(LoginRequiredMixin, FormView):
    form_class = forms.WellnessEntryForm
    template_name = "maps/wellness_form.html"
    success_url = reverse_lazy("maps:home")

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print("Block processed.")
        return super().form_valid(form)


WellnessEntryCreateView = WellnessEntryCreate.as_view()
