# set up and dependencies
from flask import Flask, render_template,request,jsonify
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import inspect
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
import os


# establish connection string
connection_str = f"postgres://postgres:0ug4NpsEC1IxLOwm@35.226.67.191:5432/project2"

#set up database
engine = create_engine(connection_str)

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# save refrences to each table
airport_delays = Base.classes.airport_delays

# Create session link from python to DB
session = Session(engine)
#############

# Flask Setup

app = Flask(__name__)

# create home page route - Test
# @app.route("/")
# def index():
#     return (
#         f"TEST<br>"
#         f"TEST AGAIN <br>"
#     )

# create home page route
@app.route("/")
def index():
    # title = "Airline Stats and Visualizations"
    return render_template("test_copy.html")


@app.route("/display")
def display():
   result = cursor.fetchall()
   #results = session.query(flights_metadata).all()
   return jsonify(result)


@app.route("/routes")
def routes():
    return render_template("routes.html")

@app.route("/visuals")
def visuals():
    return render_template("visuals.html")

@app.route("/traffic")
def traffic():
    return render_template("traffic.html")

@app.route("/performance")
def performance():
    return render_template("performance.html")

@app.route("/team")
def team():
    return render_template("team.html")

if __name__ == "__main__":
    app.run(debug=True,port=5001)

