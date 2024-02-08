# tasks.py

from celery import Celery
from serve import create_connection  # Import the connection function

celery = Celery(__name__, broker='redis://localhost:6380')

@celery.task
def generate_csv(venue_id):
    import csv
    try:
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM venues WHERE id = ?', (venue_id,))
        theater_data = cursor.fetchone()

        if not theater_data:
            return "Theater not found"

        csv_filename = f"theater_{venue_id}.csv"
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Theater ID', 'Name', 'Location', 'City', 'Count'])
            csv_writer.writerow(theater_data)

        return f"CSV for Theater ID {venue_id} generated successfully: {csv_filename}"
    except Exception as e:
        return f"Error generating CSV for Theater ID {venue_id}: {str(e)}"
    finally:
        conn.close()



# from celery.schedules import crontab

# celery.conf.beat_schedule = {
#     'generate-monthly-report': {
#         'task': 'tasks.generate_monthly_report',
#         'schedule': crontab(day_of_month='1', hour=0, minute=0),
#     },
# }
