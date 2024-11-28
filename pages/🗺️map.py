import os
import leafmap.foliumap as leafmap
import streamlit as st
import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk

st.set_page_config(layout="wide")
st.title("map a")

with st.expander("See source code"):
  with st.echo():
    m=leafmap.Map(center=[23.5, 121], zoom=7)
    path="https://raw.githubusercontent.com/liuchia515/gisapp_hw10/main/difference_result.geojson"
    m.add_geojson(path,layer_name="difference")
m.to_streamlit(height=500)
