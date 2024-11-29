import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd

st.set_page_config(layout="wide")
st.title("📌station point")
mardown1="20180206地震各測站位置以及觀測數值"
st.markdown(mardown1)

with st.expander("See source code"):
    with st.echo():
      m = leafmap.Map(center=[23.5,121], zoom=7, minimap_control=True)
      data = "https://raw.githubusercontent.com/liuchia515/gisapp_hw10/refs/heads/main/station.csv"
      m.add_points_from_xy(
        data,
        x="lon",
        y="lat",
        spin=True,
      ) 
m.to_streamlit(height=700)
st.dataframe(data)
