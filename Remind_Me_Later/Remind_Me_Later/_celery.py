from __future__ import absolute_import

from celery import Celery
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Remind_Me_Later.settings')
from django.conf import settings
app = Celery('Remind_Me_Later.tasks',
             broker='django://',
             backend='',
             include=['tasks'],
             CELERY_RESULT_BACKEND = ""
             )

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    app.start()