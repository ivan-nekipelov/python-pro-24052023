import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dealership.settings")

celery_app = Celery("dealership")

celery_app.config_from_object("django.conf:settings", namespace="CELERY")

celery_app.autodiscover_tasks()


@celery_app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
