from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
# set the default Django settings module for the 'celery' program.
app = Celery('fight_covid19')


# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))


# DEBUG CELERY BEAT TASK
# from celery.decorators import periodic_task
# from datetime import timedelta

# @periodic_task(run_every=timedelta(seconds=2))
# def every_2_seconds():
#     print("Running periodic task!")