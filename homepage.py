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
m=leafmap.Map(minimap_control=True,center=[23.5, 121], zoom=7)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)

st.markdown(
  """
  1973年後，規模5以上的地震分布
  """
)
st.image("ML_map.png", caption="ML_map")
