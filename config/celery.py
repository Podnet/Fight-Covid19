from __future__ import absolute_import

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
from celery import Celery
from . import celery_config
from config.celery_config import INCLUDE_TASKS_PATH

# set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')

app = Celery("fight_covid19", include=INCLUDE_TASKS_PATH)
# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object(celery_config)


app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))


# DEBUG CELERY BEAT TASK
# from celery.decorators import periodic_task
# from datetime import timedelta

# @periodic_task(run_every=timedelta(seconds=2))
# def every_2_seconds():
#     print("Running periodic task!")
