from flask_app import app
from models import StationName
from flask import render_template



@app.route('/')
def index():
    all_stations = StationName.query.all()
    one_item = StationName.query.filter_by(id=456).first()
    return render_template('showfirst.html', one_item=one_item, all_stations=all_stations)

@app.route('/make_name', methods=['POST'])
def make_name():
    return render_template('results.html')





