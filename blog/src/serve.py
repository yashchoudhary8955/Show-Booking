from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS
from celery_worker import make_celery
from celery import Celery


app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False

import sqlite3

def create_connection():
    return sqlite3.connect('./venues.db')

connection = create_connection()

#from flask import Celery

flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL='redis://localhost:6380',
    CELERY_RESULT_BACKEND='redis://localhost:6380'
)
celery = Celery(__name__, broker='redis://localhost:6380')
celery.config_from_object(flask_app.config)

@celery.task()
def add_together(a, b):
    return a + b



@app.route('/api/addVenue', methods=['POST'])
def add_venue():
    data = request.json
    name = data.get('name')
    location = data.get('location')
    city = data.get('city')
    count = data.get('count')

    if not all([name, location, city, count]):
        return jsonify(error='Please provide all required fields.'), 400

    try:
        conn = sqlite3.connect('venues.db')  # Change to your database connection
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO venues (name, location, city, count) VALUES (?, ?, ?, ?)',
            (name, location, city, count)
        )
        conn.commit()
        conn.close()
        return jsonify(message='Venue added successfully.'), 201
    except Exception as e:
        print("Error:", str(e))  # Print the error message
    import traceback
    traceback.print_exc()     # Print the full traceback
    return jsonify(error='Failed to add the venue.'), 500


# Endpoint to get the list of venues
@app.route('/api/getVenuess', methods=['GET'])
def get_venuess():
    try:
        conn = sqlite3.connect('venues.db')  # Change to your database connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM venues')
        venues = cursor.fetchall()
        conn.close()
        return jsonify(venues), 200
    except Exception as e:
        return jsonify(error='Failed to fetch venues.'), 500

# Endpoint to add a new show for a venue
@app.route('/api/addshow/<int:venueId>', methods=['POST'])
def add_show(venueId):
    data = request.json
    name = data.get('name')
    rating = data.get('rating')
    timing = data.get('timing')
    tags = data.get('tags')
    price = data.get('price')
    count = data.get('count')

    if not all([name, rating, timing, tags, price]):
        return jsonify(error='Please provide all required fields for the show.'), 400

    try:
        conn = sqlite3.connect('venues.db')  # Change to your database connection
        cursor = conn.cursor()
        cursor.execute(
    'INSERT INTO shows (venue_id, name, rating, timing, tags, price, count) VALUES (?, ?, ?, ?, ?, ?, ?)',
    (venueId, name, rating, timing, tags, price, count)
)

        conn.commit()
        conn.close()
        return jsonify(message='Show added successfully.'), 201
    except Exception as e:
        print(e)
        return jsonify(error='Failed to add the show.'), 500


@app.route('/api/updateVenue/<int:venue_id>', methods=['PUT'])
def update_venue(venue_id):
    updated_data = request.get_json()

    # Update the venue in the database
    conn = sqlite3.connect('venues.db')
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE venues
        SET name = ?, location = ?, city = ?, count = ?
        WHERE id = ?
        """,
        (updated_data['name'], updated_data['location'], updated_data['city'], updated_data['count'], venue_id)
    )
    conn.commit()

    # Check if the update was successful
    if cursor.rowcount > 0:
        return jsonify({'message': 'Venue updated successfully'})
    else:
        return jsonify({'error': 'Venue not found'}), 404


# Endpoint to update a show for a venue
@app.route('/api/updateshow/<int:showId>', methods=['PUT'])
def update_show(showId):
    data = request.json
    name = data.get('name')
    rating = data.get('rating')
    timing = data.get('timing')
    tags = data.get('tags')
    price = data.get('price')
    count = data.get('count')

    if not all([name, rating, timing, tags, price]):
        return jsonify(error='Please provide all required fields for the show.'), 400

    try:
        conn = sqlite3.connect('venues.db')  # Change to your database connection
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE shows SET name = ?, rating = ?, timing = ?, tags = ?, price = ?,count=? WHERE id = ?',
            (name, rating, timing, tags, price,count, showId)
        )
        conn.commit()
        conn.close()
        return jsonify(message='Show updated successfully.'), 200
    except Exception as e:
        return jsonify(error='Failed to update the show.'), 500


@app.route('/')
def index():
    return "Welcome to the Venue Booking API"

@app.route('/api/getVenues', methods=['GET'])
def get_venues():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        #print(cursor.execute('.table'))

        query = """
        SELECT v.id AS venue_id, v.name AS venue_name, v.location, v.city, v.count,
               s.id AS show_id, s.name AS show_name, s.rating, s.timing, s.tags, s.price
        FROM venues v
        INNER JOIN shows s ON v.id = s.venue_id
        """
        
        cursor.execute(query)
        rows = cursor.fetchall()
        
        venues = {}
        
        for row in rows:
            venue_id, venue_name, location, city, count, show_id, show_name, rating, timing, tags, price = row
            
            if venue_id not in venues:
                venues[venue_id] = {
                    'id': venue_id,
                    'name': venue_name,
                    'location': location,
                    'city': city,
                    'count': count,
                    'shows': []
                }
            
            if show_id:
                venues[venue_id]['shows'].append({
                    'id': show_id,
                    'name': show_name,
                    'rating': rating,
                    'timing': timing,
                    'tags': tags,
                    'price': price,
                    'available_tickets': count
                })
        
        venues_list = list(venues.values())
        return jsonify(venues_list)
    
    except Exception as e:
        print('Error fetching venues and shows:', e)
        return jsonify({'error': 'Internal server error'}), 500
    finally:
        conn.close()

@app.route('/api/venues/<int:venueId>/shows/<int:showId>/book', methods=['POST'])
def book_tickets(venueId, showId):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        tickets = request.json.get('tickets')

        if not tickets or not isinstance(tickets, int) or tickets <= 0:
            return jsonify({'error': 'Invalid number of tickets'}), 400

        cursor.execute('SELECT count FROM venues WHERE id = ?', (venueId,))
        row = cursor.fetchone()

        if not row:
            return jsonify({'error': 'Show not found'}), 404

        available_tickets = int(row[0])
        if available_tickets < tickets:
            return jsonify({'error': 'Not enough tickets available'}), 400

        cursor.execute('UPDATE shows SET count = count - ? WHERE id = ?', (tickets, showId))
        conn.commit()

        return jsonify({'message': 'Booking successful'})
    
    except Exception as e:
        print('Error booking tickets:', e)
        return jsonify({'error': 'Internal server error'}), 500
    finally:
        conn.close()

from flask import jsonify




@app.route('/api/getBookedShows', methods=['GET'])
def get_booked_shows():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = """
        SELECT v.name AS venue_name, s.name AS show_name, s.count AS tickets_booked
        FROM venues v
        INNER JOIN shows s ON v.id = s.venue_id
        WHERE s.count > 0
        """
        
        cursor.execute(query)
        rows = cursor.fetchall()
        
        booked_shows = []

        for row in rows:
            venue_name, show_name, tickets_booked = row
            booked_shows.append({
                'venueName': venue_name,
                'showName': show_name,
                'ticketsBooked': tickets_booked
            })

        return jsonify(booked_shows)
    
    except Exception as e:
        print('Error fetching booked shows:', e)
        return jsonify({'error': 'Internal server error'}), 500
    finally:
        conn.close()




#from tasks import generate_csv
#from celery import Celery
#from tasks import celery,generate_csv

@app.route('/api/exportTheaterCSV/<int:venueId>', methods=['GET'])
def export_theater_csv(venueId):
    from tasks import generate_csv
    # Trigger the Celery task to generate the CSV
    generate_csv.apply_async(args=[venueId])

    # Send a response to the user
    return jsonify(message=f"CSV export initiated for Theater ID {venueId}. You'll be notified when it's done.")




from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import os

# Assuming you have a 'templates' directory where your HTML templates are stored
template_env = Environment(loader=FileSystemLoader('templates'))

@celery.task
def generate_monthly_report():
    try:
        # Get the current month and year
        current_date = datetime.now()
        year = current_date.year
        month = current_date.month

        # Fetch data from your database for the given month
        # Replace this with your actual database query
        report_data = fetch_monthly_report_data(year, month)

        # Render the data into the HTML template
        template = template_env.get_template('monthly_report_template.html')
        html_report = template.render(report_data=report_data)

        # Save the HTML report to a file
        report_filename = f"monthly_report_{year}_{month}.html"
        report_path = os.path.join('reports', report_filename)
        with open(report_path, 'w',encoding='utf-8') as report_file:
            report_file.write(html_report)

        return report_path
    except Exception as e:
        return f"Error generating monthly report: {str(e)}"

def fetch_monthly_report_data(year, month):
    # Fetch your data from the database based on the year and month
    # Replace this with your actual database query
    # Return the data as a dictionary to be used in the template
    return {
        'month': month,
        'year': year,
        'bookings': [...],  # List of bookings
        'shows': [...],     # List of shows
        'ratings': {...}    # Ratings data
    }


# app.py
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_username'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@celery.task
def send_monthly_report_email(report_file):
    msg = Message("Monthly Entertainment Report",
                  sender="from@example.com",
                  recipients=["to@example.com"])
    msg.html = "Here's your monthly progress report!"
    with app.open_resource(report_file) as report:
        msg.attach("report.html", "text/html", report.read())
    mail.send(msg)



from datetime import timedelta
#from tasks import generate_monthly_report
celery = Celery(__name__, broker='redis://localhost:6380')
celery.conf.beat_schedule = {
    'generate_monthly_report_task': {
        'task': 'tasks.generate_monthly_report',
        'schedule': timedelta(days=1),  # Run the task on the first day of each month
    },
}
celery.conf.timezone = 'UTC'


if __name__ == '__main__':
    app.run(port=3002,debug=True)
