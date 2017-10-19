from flask_app import app
from models import StationName



@app.route('/')

def index():
    first_station = StationName.query.first()
    return '<h1>The first station is: ' + str(first_station.id) + '</h1>'