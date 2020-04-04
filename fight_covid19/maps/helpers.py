import requests
from django.conf import settings
from django.db.models import Q

from fight_covid19.maps.models import HealthEntry


def get_stats():
    data = dict()
    statewise = dict()  # To store total stats of the state
    last_updated = dict()
    total_people = HealthEntry.objects.all().order_by("user").distinct("user_id")
    data["sickPeople"] = sick_people = total_people.filter(
        Q(fever=True) | Q(cough=True) | Q(difficult_breathing=True)
    ).count()
    data["totalPeople"] = total_people.count()
    data["shortnessOfBreath"] = total_people.filter(Q(difficult_breathing=True)).count()
    data["fever"] = total_people.filter(Q(fever=True)).count()

    r = requests.get(settings.COVID19_STATS_API)
    if r.status_code == 200:
        r_data = r.json()
        india_stats = r_data
        total_stats = dict()  # To store total stats of the country
        total_stats.update(india_stats["statewise"][0])
        total_stats["deltaactive"] = india_stats["statewise"][0]["delta"]["active"]
        for i in india_stats["statewise"][1:]:
            statewise[i["state"]] = i
            statewise[i["state"]]["deltaactive"] = i["delta"]["active"]
        data.update(total_stats)
        last_updated = india_stats["tested"][-1]
    return data, statewise, last_updated


def get_map_markers():
    points = (
        HealthEntry.objects.all()
        .order_by("user", "-creation_timestamp")
        .distinct("user")
        .values("user_id", "latitude", "longitude")
    )
    return list(points)
