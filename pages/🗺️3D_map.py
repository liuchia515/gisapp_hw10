import os
import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

st.set_page_config(layout="wide", page_title="taiwan earthquake 3d map")
path="https://github.com/liuchia515/gisapp_hw10/blob/main/difference_result.geojson"

m = leafmap.Map(center=[23.5, 121], zoom=7)
m.add_geojson(path,layer_name="difference")
m.to_streamlit(height=500)
