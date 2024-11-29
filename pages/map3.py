import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(layout="wide")
st.title("🗺️map3")

path = "https://raw.githubusercontent.com/liuchia515/gisapp_hw10/refs/heads/main/GDMScatalog.csv"
data = pd.read_csv(
  path,
  names=["date","time","lat","lon","depth","ML",], 
)
st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=23.5,
            longitude=121,
            zoom=7,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=data,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
        ],
    )
)
