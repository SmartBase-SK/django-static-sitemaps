from celery import shared_task, current_app
from celery.schedules import crontab

from static_sitemaps import conf
from static_sitemaps.generator import SitemapGenerator

__author__ = 'xaralis'

# Create class conditionally so the task can be bypassed when repetition 
# is set to something which evaluates to False.
if conf.CELERY_TASK_SCHEDULE:
    current_app.conf.beat_schedule.update({
        'generate_sitemaps': {
            'task': 'generate_sitemap',
            'schedule': crontab()
        },
    })


@shared_task(name='generate_sitemap')
def generate_sitemap(verbosity=1):
    generator = SitemapGenerator(verbosity=verbosity)
    generator.write()
