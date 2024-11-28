import os
import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

st.set_page_config(layout="wide", page_title="taiwan earthquake 3d map")
path="https://github.com/liuchia515/gisapp_hw10/blob/main/difference_result.geojson"

m = leafmap.Map(center=[23.5, 121], zoom=7)
m.add_geojson(
    path,
    layer_type="fill-extrusion",
    name="difference",
    paint={
        "fill-extrusion-color": ["get", "color"],
        "fill-extrusion-height": ["*", ["get", "difference"], 50],
        "fill-extrusion-opacity": 0.8,
    },
)
m.add_colorbar(
    cmap="coolwarm",
    label="Difference",
    orientation="horizontal",

)
m.to_streamlit(height=500)
