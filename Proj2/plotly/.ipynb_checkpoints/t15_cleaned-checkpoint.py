import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df1 = pd.read_csv("../db/final_topairports_metadata.csv")

yearly_group = (
    df1.groupby(["flight_year", "airport", "Latitude", "Longitude"], as_index=False)
    .sum()
    .drop(columns=["uid", "flight_month"])
)

airport_group = (
    df1.groupby(["airport", "Latitude", "Longitude"], as_index=False)
    .sum()
    .drop(columns=["uid", "flight_month", "flight_year"])
    .sort_values("arr_flights", ascending=False)
)

yearly_group.to_csv("../db/yearly_group.csv", index=False)
airport_group.to_csv("../db/airport_group.csv", index=False)