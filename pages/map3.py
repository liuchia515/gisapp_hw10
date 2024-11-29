import pydeck as pdk
import streamlit as st

st.set_page_config(layout="wide")
st.title("🗺️map3")

url = "https://raw.githubusercontent.com/liuchia515/gisapp_hw10/main/difference_result.geojson"
INITIAL_VIEW_STATE = pdk.ViewState(latitude=23.5, longitude=121, zoom=7, max_zoom=16, pitch=45, bearing=0)
geojson = pdk.Layer(
  "GeoJsonLayer",
  url,
  opacity=0.8,
  stroked=False,
  filled=True,
  extruded=True,
  wireframe=True,
  get_elevation="difference",
  get_fill_color="color",
  get_line_color=[255,255,255],
)
r=pdk.Deck(layers=geojson,initial_view_state=INITIAL_VIEW_STATE)
r.to_html("geojson_layer.html")
