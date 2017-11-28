#Dependencies
from flask import Flask,jsonify

import datetime as datetime
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

####################################################################
# Database Setup
####################################################################

# Create Engine
engine = create_engine("sqlite:///belly_button_biodiversity.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Biodiversity = Base.classes.biodiversity

# Create our session (link) from Python to the DB
session = Session(engine)

#####################################################################
# Flask Setup
#####################################################################

app = Flask(__name__)

#####################################################################
# Flask Routes
#####################################################################


@app.route('/')
def dashboard():
    """Return the dashboard homepage"""
    return(index.html)(
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/passengers"
    )

@app.route('/names')
def samplenames():
    """Returns a list of sample names in the format"""
    # Query all Belly Button Biodiversity
    results = session.query(Biodiversity.name).all()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    # print(all_names)
    return jsonify(all_names)

@app.route('/otu')
def otudescriptions():
    """Returns a list of OTU descriptions in the following format"""
    
    # Query all passengers
    results = session.query(Biodiversity).all()

    #Create a dictionary from the row data and append to a list 
    all_passengers = []
    for passengers in results:
        passengers_dict = {}
        passengers_dict["name"] = passengers.name
        passengers_dict["age"] = passengers.age
        passengers_dict["sex"] = passengers.sex
        all_passengers.append(passengers_dict)
    return jsonify(all_passengers)

@app.route('/metadata/<sample>')
def jsonify():
    results = session.query(Passengers).filter(Passenger.survived == 1)
    """Returns a json dictionary of sample metadata in the format"""
    
    survived_passengers = []
    for passengers in results:
        # if (passenger.survived ==1):
        passenger_dict = {}
        passenger_dict["name"] = passenger.name
        survived_passengers.append(passenger_dict)
    return jsonify(survived_passengers)

@app.route('/wfreq/<sample>')
def WFREQ():
    """Returns an integer value for the weekly washing frequency `WFREQ`"""
    return jsonify()

@app.route('/sample/<sample>')
def dictionaries():
    """Return a list of dictionaries containing sorted lists  for `otu_ids`
    and `sample_values`""" 
    return jsonify()

@app.route()
def dictionaries2():
    """Return a list of dictionaries containing sorted list for 'sample_values'"""
    return jsonify()

if __name__ == '__main__':
    app.run(debug=True)