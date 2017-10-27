from app import app
from models import StationName
from flask import Flask, render_template, jsonify, request
import random
from name_generator import namegen
import pyttsx3

# gen123 = namegen()
engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel')

@app.route('/')
def index():
	return render_template('index.html')

@app.route("/name_test/", methods=['POST'])
def name_test():
    announcement = 'This is the train to... Horton Buxley. Serving, Dibbon Town, Fennington Brin, Wensleyford, Dibbon Rake, Wawlend, Wensleyford Sutton... and Horton Buxley... The next stop, is Dibbon Rake'


    # names = gen123.prepare_text() # insane to have this executing every time, but will probably be working from db anyway
    # ngrams = gen123.create_ngrams_dict(names)
    # onename = gen123.markov_it(names, ngrams)
    engine.say(announcement)
    engine.runAndWait()
    return jsonify({'data': render_template('response.html', station_name='placeholder')})


# Below method is adapted from a tutorial and shows the basics of how to access 
# info from a db and send to a template

# def index():
#     all_stations = StationName.query.all()
#     one_item = StationName.query.filter_by(id=456).first()
#     return render_template('showfirst.html', one_item=one_item, all_stations=all_stations)

# @app.route('/make_name', methods=['POST'])
# def make_name():
#     return render_template('results.html')





