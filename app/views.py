from app import app
from models import StationName
from flask import Flask, render_template, jsonify, request
import random
from name_generator import namegen
#import pyttsx3

# gen123 = namegen()
#engine = pyttsx3.init()
#engine.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel')

@app.route('/')
def new_approach():
    return render_template('new_approach.html')

# @app.route('/')
# def index():
# 	return render_template('index.html')
#
# @app.route("/name_test/", methods=['POST'])
# def name_test():
#     announcement = 'This is the train to... Horton Buxley. Serving, Dibbon Town, Fennington Brin, Wensleyfurd, Dibbon Rake, Wawlend, Wensleyfurd Sutton... and Horton Buxley... The next stop, is Dibbon Rake'
#     announcement2 = 'This is the trayn to... Cotshyre Broadway. Serving Marbot Central, Cronebury Paps, East Worton, Bingnam Rye, Worton Cross Junction, Carlton Upon Wilkes... and Cotshyre Broadway... The next stop, is East Worton'
#     announcement3 = 'This is the train to... Wurgait on Sea. Serving, Banner Bridge, Brookton Abbey, Brookton Weir, Stove, Pembel-ton Weir, Frommich on Sea, Boxely... and Wurgait on Sea... The next stop, is Banner Bridge'
#     announcement4 = 'This is the train to... Morpatch Sudden. Serving, Rainhill Park, Tuxton Court, Waddon, Tuxton Moor, Brimly, Plaisfurd Juction, River, Morpatch East, Ploonfoot Way... and Morpatch Sudden... The next stop, is Rainhill Park'
#     #announcement5 = 'This is the train to... Wigney Patch. Serving, Rajley, Hodden Street, Kiteshead Green, Kiteshead Rajley, Wigney Chase, Boorsbutton... and Wigney Patch... The next stop, is Rajley'
#     # names = gen123.prepare_text() # insane to have this executing every time, but will probably be working from db anyway
#     # ngrams = gen123.create_ngrams_dict(names)
#     # onename = gen123.markov_it(names, ngrams)
#     names = ['Horton Buxley', 'Dibbon Town', 'Fennington Brin', 'Wensleyford', 'Dibbon Rake', 'Wallend', 'Wensleyford Sutton', 'Cotshire Broadway', 'Marbot Central', 'Cronebury Paps', 'East Worton', 'Bingam Rye', 'Worton Cross Junction', 'Carlton Upon Wilkes', 'Corbleton Rye', 'Cotshire Mindle' ]
#     # engine.say(announcement4)
#     # engine.runAndWait()
#     # engine.endLoop()
#     return jsonify({'data': render_template('voicetest.html', station_name=names[random.randint(0, len(names)-1)])})


# Below method is adapted from a tutorial and shows the basics of how to access 
# info from a db and send to a template

# def index():
#     all_stations = StationName.query.all()
#     one_item = StationName.query.filter_by(id=456).first()
#     return render_template('showfirst.html', one_item=one_item, all_stations=all_stations)

# @app.route('/make_name', methods=['POST'])
# def make_name():
#     return render_template('results.html')





