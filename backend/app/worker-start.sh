#! /usr/bin/env bash
python /app/app/celeryworker_pre_start.py

# celery worker -A app.worker -l info -Q main-queue -c 1
# python manage.py run celery
# argv = ['worker', '--pool=gevent', '-lINFO', '-Qdata,signal,database,position,engine,starter', '--concurrency=10000']
celery -A pedesis.tasks_manager:manager worker --pool=gevent -l INFO --concurrency=10000
