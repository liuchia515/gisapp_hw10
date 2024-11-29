import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")
st.title("📌station point")

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
