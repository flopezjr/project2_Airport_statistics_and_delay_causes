import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

airport_group = pd.read_csv("../db/airport_group.csv")
yearly_group = pd.read_csv("../db/yearly_group.csv")

fig = px.scatter_geo(
    yearly_group,
    lat="Longitude",
    lon="Latitude",
    animation_frame="flight_year",
    color="arr_flights",
    size="arr_flights",
    scope="usa",
    hover_name="airport",
    size_max=30,
    color_continuous_scale=px.colors.sequential.Bluered,
    labels={"arr_flights": "Delayed Flights", "flight_year": "Year"},
)

fig.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)
fig.update_layout(title_text="United States Top Busiest Airports by Year (2013 - 2018)")



fig = px.scatter_geo(
    airport_group,
    lat="Longitude",
    lon="Latitude",
    color="airport",
    size="arr_flights",
    scope="usa",
    hover_name="airport",
    size_max=30,
    color_continuous_scale=px.colors.sequential.Bluered,
    labels={"airport": "Airports", "arr_flights": "Delayed Flights"},
    text="airport",
)

fig.add_trace(
    go.Scattergeo(
        lon=airport_group["Latitude"],
        lat=airport_group["Longitude"],
        text=airport_group["airport"],
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

fig.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)
fig.update_layout(title_text="United States Top Busiest Airports Total (2013 - 2018)")

