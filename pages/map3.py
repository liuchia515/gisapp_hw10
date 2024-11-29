import os
import altair as alt
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(layout="wide")
st.title("🗺️map3")
@st.cache_resource
def load_data():
  path = "https://raw.githubusercontent.com/liuchia515/gisapp_hw10/refs/heads/main/GDMScatalog.csv"
  data = pd.read_csv(
    path,
    names=["date","time","lat","lon","depth","ML",], 
    skiprows=1,
  )
  return data

def map(data, lat, lon, zoom):
    st.write(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state={
                "latitude": lat,
                "longitude": lon,
                "zoom": zoom,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=data,
                    get_position=["lon", "lat"],
                    radius=100,
                    elevation_scale=4,
                    elevation_range=[0, 10],
                    pickable=True,
                    extruded=True,
                ),
            ],
        )
    )
data = load_data()
