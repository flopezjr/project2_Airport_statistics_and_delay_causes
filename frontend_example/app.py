from flask import Flask, jsonify, render_template
import csv
import pandas as pd
import os
import json
import plotly
import plotly.graph_objects as go
import plotly.express as px

app = Flask(__name__)

def load_data():
    yearly_grouped = pd.read_csv("db/yearly_group.csv")
    return yearly_grouped

def airport_data():
    airport_grouped = pd.read_csv("db/airport_group.csv")
    return airport_grouped

def year_carrier_data():
    year_carrier = pd.read_csv("db/year_carrier.csv")
    return year_carrier

def create_plot_express():
    data = load_data()
    fig1 = px.scatter_geo(
        data,
        lat="Longitude",
        lon="Latitude",
        animation_frame="flight_year",
        color="arr_flights",
        size="arr_flights",
        scope="usa",
        size_max=50,
        hover_name="airport",
        color_continuous_scale=px.colors.sequential.Bluered,
        labels={"arr_flights": "Delayed Flights", "flight_year": "Year"},
    )
    
    fig1.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)
    fig1.update_layout(title_text="United States Top Busiest Airports by Year (2013 - 2018)")

    return json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

def airport_plot():
    data = airport_data()
    fig2 = px.scatter_geo(
        data,
        lat="Longitude",
        lon="Latitude",
        color="airport",
        size="arr_flights",
        scope="usa",
        hover_name="airport",
        size_max=50,
        color_continuous_scale=px.colors.sequential.Bluered,
        labels={"airport": "Airports", "arr_flights": "Delayed Flights"},
        
    )

    fig2.add_trace(
        go.Scattergeo(
            lon=data["Latitude"],
            lat=data["Longitude"],
            text=data["airport"],
            textposition=[
                "middle center",
                "middle center",
                "middle center",
                "middle center",
                "middle center",
                "middle center",
                "middle center",
                "middle center",
                "middle center",
                "top left",
                "middle center",
                "middle center",
                "middle center",
                "middle center",
                "bottom right",
            ],
            mode="text",
            showlegend=False,
        )
    )

    fig2.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)
    fig2.update_layout(title_text="United States Top Busiest Airports Total (2013 - 2018)")

    return json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

def year_carrier_plot():
    data = load_data()
    fig3 = px.scatter(
        data,
        x="arr_flights",
        y="arr_delay",
        animation_frame="flight_year",
        animation_group="airport",
        color="carrier",
        size="carrier_ct",
        hover_name="airport",
        size_max=30,
        labels={
            "carrier": "Carrier",
            "flight_year": "Flight Year",
            "airport": "Airport",
            "arr_flights": "Num. of Delayed Flights",
            "arr_delay": "Delay Time (Hours)",
            "carrier_ct": "Air Carrier Delay",
        },
        title="Time Delayed (Hours) by Carrier and Airport (2013 - 2017)",
        height=700,
        range_x=[-1000, 80000],
        range_y=[-1000, 20000],
    )

    return json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

def total_delay_bar():
    data = airport_data()
    fig4 = px.bar(
        data,
        x="airport",
        y="arr_flights",
        labels={
            "carrier": "Carrier",
            "flight_year": "Flight Year",
            "airport": "Airport",
            "arr_flights": "Num. of Delayed Flights",
            "arr_delay": "Delay Time (Hours)",
            "carrier_ct": "Air Carrier Delay",
        },
        title="Total Delayed Flight by Airport (2013 - 2018)",
        text="arr_flights",
)
    fig4["layout"].pop("updatemenus")


    return json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)


@app.route("/")
def home():
    fig1 = create_plot_express()
    return render_template("index.html", fig1=fig1)

@app.route("/express")
def express():
    fig2 = airport_plot()
    return render_template("express.html", fig2=fig2)

@app.route("/year_carrier")
def year_carrier():
    fig3 = year_carrier_plot()
    return render_template("scatyear_carrierter.html", fig3=fig3)

@app.route("/total_delay")
def total_delay():
    fig4 = total_delay_bar()
    return render_template("total_delay.html", fig4=fig4)



if __name__ == "__main__":
    app.run(debug=True)