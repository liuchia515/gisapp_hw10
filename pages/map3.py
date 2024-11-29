import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")
st.title("🗺️map3")

with st.expander("See source code"):
    with st.echo():
        filepath = "https://raw.githubusercontent.com/liuchia515/gisapp_hw10/main/difference_result.geojson"
        m = leafmap.Map(center=[23.5, 121], zoom=7)
        m.add_heatmap(
            filepath,
            value="difference",
            name="Heat map",
            radius=20,
        )
m.to_streamlit(height=700)
