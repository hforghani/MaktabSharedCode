import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery.settings")
app = Celery("django_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # Scheduler Name
    'print-message-ten-seconds': {
        # Task Name (Name Specified in Decorator)
        'task': 'print_msg_main',
        # Schedule
        'schedule': 10.0,
        # Function Arguments
        'args': ("Hello",)
    },
}
