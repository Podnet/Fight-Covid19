import requests
from django.conf import settings
from django.db.models import Q
from fight_covid19.maps.models import HealthEntry
from fight_covid19.maps.utils import GeoLocation


def get_stats():
    data = dict()
    data["sickPeople"] = sick_people = HealthEntry.objects.filter(
        Q(fever=True) | Q(cough=True) | Q(difficult_breathing=True)
    ).count()
    data["totalPeople"] = (
        HealthEntry.objects.all().order_by("user").distinct("user_id").count()
    )
    r = requests.get(settings.COVID19_STATS_API)
    if r.status_code == 200:
        r_data = r.json()
        india_stats = list(filter(lambda x: x["country"] == "India", r_data))
        data.update(india_stats[0])
    return data


def get_map_markers():
    points = (
        HealthEntry.objects.all()
        .order_by("user", "-creation_timestamp")
        .distinct("user")
        .values("user_id", "latitude", "longitude")
    )
    return list(points)



def get_range_coords(deg_lat, deg_long, radius=5):
    '''
    Takes coordinates in degrees with optional radius value (default=5)
    Returns a list of min & max longitudes and latitudes
    '''
    location = GeoLocation.from_degrees(deg_lat, deg_long)
    sw_pos, ne_pos = location.distance(radius)
    # X => long
    # Y => lat
    return {
        'min_lon': sw_pos.deg_lon, 
        'min_lat': sw_pos.deg_lat,
        'max_lon': ne_pos.deg_lon,
        'max_lat': ne_pos.deg_lat,
    }
