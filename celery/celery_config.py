from celery import Celery

app = Celery('celery_config',
             broker='redis://localhost:6379/0',
             include=['task.celery_blog', 'task.celery_add'])
