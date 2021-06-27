#from flask import Flask

#app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello world'

#RUN THIS IN TERMINAL:
# export FLASK_APP=app.py
# flask run
## SHOULD RETURN A "Running on" folled by adress and port #
### A port number is essentially the endpoint of a given program or service. 
### Any Flask application you create can have whatever port number you would like, but the most common is 5000.
### Copy and paste your localhost address into your web browser. Generally, a localhost will look something like this, for context.
##RETURNS SOMETHING LIKE THIS--- localhost:5000


import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#Setting Up Database
engine = create_engine("sqlite:///hawaii.sqlite")

#The create_engine() function allows us to access and query our SQLite database file. Now let's reflect the database into our classes.
Base = automap_base()
##Python Flask--Reflect table function is Base.prepare()
Base.prepare(engine, reflect=True)
##Saving quick refs to tables
Measurement = Base.classes.measurement
Station = Base.classes.station
#session link from Python to our database
session = Session(engine)
#To define our Flask app, add the following line of code. This will create a Flask application called "app."
app = Flask(__name__)
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

##  ## ## RUNNING FLASK SEPERATE FROM CODE ## ## ##

# export FLASK_APP=app.py
# flask run 

#Creating New Routes--make sure it is far left, no indent & Creating function for each##
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)