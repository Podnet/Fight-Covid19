from __future__ import absolute_import, unicode_literals

from celery import task
from celery.signals import celeryd_after_setup
from django.core.cache import cache

from fight_covid19.maps.helpers import (
    get_map_markers,
    get_covid19_stats,
    get_hoi_stats,
)


# Initial Data Load to Cache
@celeryd_after_setup.connect
def on_worker_start(sender, instance, **kwargs):
    cache.set("covid19_stats", get_covid19_stats())
    cache.set("hoi_stats", get_hoi_stats())
    cache.set("map_markers", get_map_markers())


@task()
def cache_hoi_stats():
    new_stats = get_hoi_stats()
    old_stats = cache.get("hoi_stats", None)
    if not old_stats or (new_stats != old_stats):
        cache.set("hoi_stats", new_stats)
        cache.set("map_markers", get_map_markers())


@task()
def cache_covid19_stats():
    cache.set("covid19_stats", None)
