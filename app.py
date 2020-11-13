from flask import Flask, render_template,request,jsonify
import os
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2

app = Flask(__name__)


con = psycopg2.connect(database="routes_db", user="postgres", password="", host="", port="")
cursor = con.cursor()

@app.route("/flights_delay20132018", methods=['post', 'get'])
def test():  

    cursor.execute("SELECT ROUND(AVG(arr_delay),0) AS delay, carrier_name FROM flights_metadata GROUP BY carrier_name ORDER BY delay ASC;")
    result = cursor.fetchall()
    #return render_template("showdata.html", data=result)
    return jsonify(result)

#@app.route("/flights_delay20132018/<Inputyear>", methods=['post', 'get'])
#def test():  
 #   Inputyear = int(Inputyear)
 #   cursor.execute("SELECT ROUND(AVG(arr_delay),0) AS delay, carrier_name FROM flights_metadata where year == Inputyear GROUP BY carrier_name ORDER BY delay ASC;")
  #  result = cursor.fetchall()
    #return render_template("showdata.html", data=result)
   # return jsonify(result)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:zvtP3Mg7rPac2Bee@104.154.50.101:5432/routes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

engine = create_engine("postgres://postgres:zvtP3Mg7rPac2Bee@104.154.50.101:5432/routes_db")
Base = automap_base()
Base.prepare(db.engine, reflect=True)
conn = engine.connect()
session = Session(engine)


@app.route("/")
def index():
    title = "Airline Stats and Visualizations"
    return render_template("index.html", title=title)


@app.route("/display")
def display():
   results = session.query(flights_metadata).filter_by(flights_metadata.year == '2013').all()
   #results = session.query(flights_metadata).all()
   year_list = results['year'].unique()
   return jsonify(year_list.tolist())

#@app.route("/selectdata")
#def seldata():
#    x = request.args.get('stuff')
#    mydata = sql("SELECT * FROM flights_metadata where year = :year_input;", {"year_input":x})
#    return render_template('showdata.html', target = x, mydata = mydata)
#return html

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
    app.run(debug=True)
