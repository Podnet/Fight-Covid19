import requests
from django.conf import settings
from django.db.models import Q

from fight_covid19.maps.models import HealthEntry
from fight_covid19.maps.utils import GeoLocation


def get_covid19_stats():
    data = dict()

    r = requests.get(settings.COVID19_STATS_API)
    if r.status_code == 200:
        india_stats = r.json()
        # To store total stats of the country
        data["total_stats"] = india_stats.get("statewise", list())[0]
        data["total_stats"]["deltaactive"] = str(
            int(data["total_stats"]["deltaconfirmed"])
            - int(data["total_stats"]["deltadeaths"])
            - int(data["total_stats"]["deltarecovered"])
        )

        # Number of tests performed
        data["tests_performed"] = india_stats.get("tested", list())[-1]

        # State wise data
        data["statewise"] = dict()
        for state in india_stats.get("statewise", list())[1:]:
            data["statewise"][state["state"]] = state
            data["statewise"][state["state"]]["deltaactive"] = str(
                int(data["statewise"][state["state"]]["deltaconfirmed"])
                - int(data["statewise"][state["state"]]["deltadeaths"])
                - int(data["statewise"][state["state"]]["deltarecovered"])
            )
    return data


def get_hoi_stats():
    data = dict()
    loggedin_people = HealthEntry.objects.all().order_by("user").distinct("user_id")
    oneshot_people = (
        HealthEntry.objects.all().order_by("unique_id").distinct("unique_id")
    )

    data["totalPeople"] = loggedin_people.count() + oneshot_people.count()

    data["sickPeople"] = (
        loggedin_people.filter(
            Q(fever=True) | Q(cough=True) | Q(difficult_breathing=True)
        ).count()
        + oneshot_people.filter(
            Q(fever=True) | Q(cough=True) | Q(difficult_breathing=True)
        ).count()
    )
    data["shortnessOfBreath"] = (
        loggedin_people.filter(Q(difficult_breathing=True)).count()
        + oneshot_people.filter(Q(difficult_breathing=True)).count()
    )
    data["fever"] = (
        loggedin_people.filter(Q(fever=True)).count()
        + oneshot_people.filter(Q(fever=True)).count()
    )

    return data


def get_map_markers():
    loggedin_points = list(
        HealthEntry.objects.all()
        .order_by("user", "-creation_timestamp")
        .distinct("user")
        .values(
            "id",
            "latitude",
            "longitude",
            "age",
            "gender",
            "fever",
            "cough",
            "difficult_breathing",
            "self_quarantine",
        )
    )
    oneshot_points = list(
        HealthEntry.objects.all()
        .order_by("unique_id", "-creation_timestamp")
        .distinct("unique_id")
        .values(
            "id",
            "latitude",
            "longitude",
            "age",
            "gender",
            "fever",
            "cough",
            "difficult_breathing",
            "self_quarantine",
        )
    )
    loggedin_points.extend(oneshot_points)
    return loggedin_points


def get_range_coords(deg_lat, deg_long, radius=5):
    """
    Takes coordinates in degrees with optional radius value (default=5)
    Returns a list of min & max longitudes and latitudes
    """
    location = GeoLocation.from_degrees(deg_lat, deg_long)
    sw_pos, ne_pos = location.bounding_locations(radius)
    # X => long
    # Y => lat
    return {
        "min_lon": sw_pos.deg_lon,
        "min_lat": sw_pos.deg_lat,
        "max_lon": ne_pos.deg_lon,
        "max_lat": ne_pos.deg_lat,
    }
