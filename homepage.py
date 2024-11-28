import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout='wide')

st.title("🏠_homepage")
st.markdown(
  """
  This page is homepage
  """
)

st.header("region")
m=leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
