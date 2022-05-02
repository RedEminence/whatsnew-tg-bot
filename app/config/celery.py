from celery import Celery
from celery.schedules import crontab

from config.settings import CELERY_RESULT_BACKEND, CELERY_BROKER_URL
from services.telegram import DigestSender

celery_app = Celery()
celery_app.conf.broker_url = CELERY_BROKER_URL
celery_app.conf.result_backend = CELERY_RESULT_BACKEND
celery_app.conf.beat_schedule = {
    'add-every-15-seconds': {
        'task': 'task_send_digest',
        'schedule': crontab(hour=8),
    },
}
celery_app.conf.timezone = 'Europe/Moscow'


@celery_app.task(name='task_send_digest')
def task_send_digest():
    DigestSender().run()
