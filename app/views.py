from flask_app import app
from models import StationName
from flask import Flask, render_template, jsonify, request
import random


@app.route('/')
def index():
	return render_template('index.html')

@app.route("/name_test/", methods=['POST'])
def name_test():
	#placeholder = 'Bromborough Rake'
	placeholder = random.randrange(0,100)
	return jsonify({'data': render_template('response.html', station_name=placeholder)})


# Below method is adapted from a tutorial and shows the basics of how to access 
# info from a db and send to a template

# def index():
#     all_stations = StationName.query.all()
#     one_item = StationName.query.filter_by(id=456).first()
#     return render_template('showfirst.html', one_item=one_item, all_stations=all_stations)

# @app.route('/make_name', methods=['POST'])
# def make_name():
#     return render_template('results.html')





