import leafmap.foliumap as leafmap
import streamlit as st

st.set_page_config(layout="wide")
st.title("taiwan earthquake 3d map")

with st.expander("See source code"):
  with st.echo():
    m=leafmap.Map(center[23.5,121],zoom=7)
    path="https://github.com/liuchia515/gisapp_hw10/blob/main/difference_result.geojson"
    m.add_geojson(data,layer_name="difference",add_legend=True)
m.to_streamlit(height=500)
