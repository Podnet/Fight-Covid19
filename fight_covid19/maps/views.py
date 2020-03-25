import requests
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import FormView
from django.views.generic import ListView
from fight_covid19.maps.models import WellnessEntry

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


class HealthForm(LoginRequiredMixin, FormView):
    form_class = forms.WellnessEntryForm
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
    model = WellnessEntry
    template_name = "maps/my_health.html"
    context_object_name = "entries"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by(
            "-creation_timestamp"
        )


MyHealthView = MyHealth.as_view()
