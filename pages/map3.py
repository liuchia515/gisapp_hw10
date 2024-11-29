import streamlit as st
import pydeck
import pandas as pd

st.set_page_config(layout="wide")
st.title("🗺️map3")
path = "https://raw.githubusercontent.com/liuchia515/gisapp_hw10/refs/heads/main/GDMScatalog.csv"
data = pd.read_csv(
    path,
    header=0,
    names=["date","time","lat","lon","depth","ML",],
)

point_layer = pydeck.Layer(
    "ScatterplotLayer",
    data=data,
    id="ML",
    get_position=["lon", "lat"],
    get_color="[255, 75, 75]",
    pickable=True,
    auto_highlight=True,
    get_radius="size",
)
view_state = pydeck.ViewState(
    latitude=23.5, longitude=121, controller=True, zoom=7, pitch=30
)

