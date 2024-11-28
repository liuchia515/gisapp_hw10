import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout='wide')

st.title("🏠homepage")
st.markdown(
  """
  This page is homepage
  """
)

st.header("region")
m=leafmap.Map(minimap_control=True)
m = leafmap.Map(center=[23.5, 121], zoom=7) 
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
