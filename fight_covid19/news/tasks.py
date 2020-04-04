from __future__ import absolute_import, unicode_literals
from celery import task
from fight_covid19.news.helpers import get_news
from django.core.cache import cache
from celery.signals import celeryd_after_setup

# Initial News Load to Cache
@celeryd_after_setup.connect
def on_worker_start(sender, instance, **kwargs):
    cache.set("news", get_news())


@task()
def cache_news():
    new_news = get_news()
    old_news = cache.get("news", None)
    if not old_news or (new_news != old_news):
        cache.set("news", new_news)
