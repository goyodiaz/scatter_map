import plotly.express as px
import streamlit as st

df = px.data.carshare()
fig = px.scatter_map(
    df,
    lat="centroid_lat",
    lon="centroid_lon",
    color="peak_hour",
    size="car_hours",
    color_continuous_scale=px.colors.cyclical.IceFire,
    size_max=15,
    zoom=10,
)
st.write(fig)
st.plotly_chart(fig, key="2")
