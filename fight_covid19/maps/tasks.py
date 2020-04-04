from __future__ import absolute_import, unicode_literals
from celery import task
from fight_covid19.maps.helpers import get_stats, get_map_markers
from django.core.cache import cache
from celery.signals import celeryd_after_setup

# Initial Data Load to Cache
@celeryd_after_setup.connect
def on_worker_start(sender, instance, **kwargs):
    cache.set("stats", get_stats())
    cache.set("map_markers", get_map_markers())

@task()
def cache_stats():
    new_stats = get_stats()
    old_stats = cache.get("stats",None)
    if not old_stats or ( new_stats != old_stats ):
        cache.set("stats", new_stats)
        cache.set("map_markers", get_map_markers())    