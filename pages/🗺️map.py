import os
import leafmap.foliumap as leafmap
import streamlit as st

st.set_page_config(layout="wide")
st.title("taiwan earthquake map")

with st.expander("See source code"):
  with st.echo():
    m=leafmap.Map(center=[23.5,121],zoom=7)
    path="https://github.com/liuchia515/gisapp_hw10/blob/main/difference_result.geojson"
    m.add_geojson(path,layer_name="difference")
m.to_streamlit(height=500)
