# Celery Config
import environ

env = environ.Env()
env.read_env()

BROKER_URL = env("BROKER_URL")
# CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")
CELERY_ACCEPT_CONTENT = [env("CELERY_ACCEPT_CONTENT")]
CELERY_TASK_SERIALIZER = env("CELERY_TASK_SERIALIZER")
CELERY_RESULT_SERIALIZER = env("CELERY_RESULT_SERIALIZER")
CELERY_TIMEZONE = "Asia/Calcutta"
CELERYBEAT_SCHEDULER = "django_celery_beat.schedulers.DatabaseScheduler"

# tasks.py locations
INCLUDE_TASKS_PATH = [
    "fight_covid19.maps.tasks",
    "fight_covid19.news.tasks",
]
