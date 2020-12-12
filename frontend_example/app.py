from flask import Flask, jsonify, render_template
import csv
import pandas as pd
import os
import json
import plotly
import plotly.graph_objects as go
import plotly.express as px

app = Flask(__name__)

def final_data():
    metadata = pd.read_csv("db/final_topairports_metadata.csv")
    return metadata

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
        color="arr_del15",
        size="arr_del15",
        scope="usa",
        hover_name="airport",
        size_max=50,
        color_continuous_scale=px.colors.sequential.Bluered,
        labels={"arr_del15": "Delayed Flights", "flight_year": "Year"},
        height=700,
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
        size="arr_del15",
        scope="usa",
        hover_name="airport",
        size_max=50,
        color_continuous_scale=px.colors.sequential.Bluered,
        labels={"airport": "Airports", "arr_del15": "Delayed Flights"},
        height=700,     
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
    data = year_carrier_data()
    fig3 = px.scatter(
        data,
        x="arr_del15",
        y="arr_delay",
        animation_frame="flight_year",
        animation_group="airport",
        color="carrier",
        size="arr_flights",
        hover_name="airport",
        size_max=30,
        labels={
            "carrier": "Carrier",
            "flight_year": "Flight Year",
            "airport": "Airport",
            "arr_del15": "Delayed Flights",
            "arr_delay": "Delay Time (Hours)",
            "carrier_ct": "Air Carrier Delay",
            "arr_flight": "Total Flights",
        },
        title="Time Delayed (Hours) by Carrier and Airport (2013 - 2017)",
        height=700,
    )

    return json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

def total_delay_bar():
    data = airport_data()
    fig4 = px.bar(
        data,
        x="airport",
        y="arr_del15",
        labels={
            "carrier": "Carrier",
            "flight_year": "Flight Year",
            "airport": "Airport",
            "arr_del15": "Num. of Delayed Flights",
            "arr_delay": "Delay Time (Hours)",
            "carrier_ct": "Air Carrier Delay",
        },
        title="Total Delayed Flight by Airport (2013 - 2018)",
        text="arr_del15",
)   
    fig4["layout"].pop("updatemenus")
    return json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)

def carrier_plot():
    data = final_data()
    fig5 = px.bar(
    data.groupby("carrier", as_index=False)
    .sum()
    .sort_values(by="arr_flights", ascending=False),
    x="carrier",
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

    return json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)



@app.route("/")
def home():
    fig1 = create_plot_express()
    return render_template("index.html", fig1=fig1)

@app.route("/1")
def express():
    fig2 = airport_plot()
    return render_template("express.html", fig2=fig2)

@app.route("/2")
def year_carrier():
    fig3 = year_carrier_plot()
    return render_template("3.html", fig3=fig3)

@app.route("/3")
def total_delay():
    fig4 = total_delay_bar()
    return render_template("4.html", fig4=fig4)



if __name__ == "__main__":
    app.run(debug=True)