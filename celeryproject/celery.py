import os
from celery import Celery
from datetime import timedelta
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryproject.settings')
app = Celery('celeryproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
 
app.conf.timezone = 'UTC'
 
app.conf.beat_schedule = {
    "add_first": {
        "task": "mainapp.tasks.add_first",
        "schedule": timedelta(seconds=10),
    },
}
 
app.autodiscover_tasks()