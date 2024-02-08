from celery import Celery

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

# celery_worker.py
# from celery import Celery
# from datetime import timedelta
# from tasks import generate_monthly_report

# celery = Celery(__name__, broker='redis://localhost:6380')
# celery.conf.beat_schedule = {
#     'generate_monthly_report_task': {
#         'task': 'tasks.generate_monthly_report',
#         'schedule': timedelta(days=1),  # Run the task on the first day of each month
#     },
# }
# celery.conf.timezone = 'UTC'
