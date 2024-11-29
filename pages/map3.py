import streamlit as st
import pydeck
import pandas as pd

st.set_page_config(layout="wide")
st.title("🗺️map3")

@st.cache(persist=True)
def load_data(nrows):
    df=pd.read_csv("https://raw.githubusercontent.com/liuchia515/gisapp_hw10/refs/heads/main/GDMScatalog.csv",nrows=nrows)
    return df
df=load_data(1000)

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state={
        "latitude":"lat",
        "lontitude":"lon",
        "zoom":zoom,
        "pitch":50,
    },
    layers=[
        pdk.Layer(
            "HexagonLayer",
            data=df[["ML","lat","lon"]],
            get_position=["lat","lon"],
            radius=200,
            elevation_scale=4,
            elevation_range=[0,10],
            pickable=True,
            extruded=True,
        ),
    ]))
