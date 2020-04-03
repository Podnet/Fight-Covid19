from __future__ import absolute_import, unicode_literals
from celery import task


@task()
def simple_task():
    print("Home Refresh done")


from celery.decorators import periodic_task
from datetime import timedelta


@periodic_task(run_every=timedelta(seconds=20))
def refresh_home_data():
    print("Running periodic task!")
