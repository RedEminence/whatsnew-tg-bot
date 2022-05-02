from celery import Celery

from config.settings import CELERY_RESULT_BACKEND, CELERY_BROKER_URL

celery_app = Celery()
celery_app.conf.broker_url = CELERY_BROKER_URL
celery_app.conf.result_backend = CELERY_RESULT_BACKEND
celery_app.autodiscover_tasks()
