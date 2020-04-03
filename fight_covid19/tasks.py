from __future__ import absolute_import, unicode_literals
from celery import task
from fight_covid19.maps.helpers import get_stats
from django.core.cache import cache

@task()
def cache_stats():
    cache.set("stats", get_stats())