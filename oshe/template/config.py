import os
from os import path as op

from kombu import Queue


class Config:
    INTERNAL_HOST = "localhost"
    STAGING_HOST = "localhost"
    PRODUCTION_HOST = "localhost"

    current_dir = op.dirname(op.dirname(__file__))
    database_dir = op.join(current_dir, 'data')
    os.makedirs(database_dir, exist_ok=True)
    DATABASE_URI = 'sqlite:///%s/data.sqlite' % database_dir


class CeleryConfig:
    BROKER_URL = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/1"
    CELERY_QUEUES = (
        Queue("crawl", routing_key="crawl", queue_arguments={'x-max-priority': 7}),
        Queue("parse", routing_key="parse", queue_arguments={'x-max-priority': 2}),
        Queue("store", routing_key="store", queue_arguments={'x-max-priority': 1}))
