import os
import leafmap.foliumap as leafmap
import streamlit as st
import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk

st.title("map")

with st.expander("See source code"):
  with st.echo():
    m=leafmap.Map(center=[-123.13, 49.254], zoom=11)
    path="https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/geojson/vancouver-blocks.json"
    m.add_geojson(path,name="valuePerSqm")
m.to_streamlit(height=500)
