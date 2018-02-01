from flask import Flask, render_template, jsonify, redirect
from flask import jsonify
import csv
import json
import sqlite as sql
import pandas as pd

# from __future__ import print function
import sys


app = Flask(__name__)
app.debug=True

@app.route("/")
def index():

	return render_template("index.html")

if __name__ == "__main__":

	app.run(debug=True)