import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")
st.title("歷史地震Heatmap")

col1,col2=st.columns([4,1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")
with col2:

    basemap = st.selectbox("Select a basemap:", options, index)

with col1:
    with st.expander("See source code"):
        with st.echo():
            filepath = "https://raw.githubusercontent.com/liuchia515/gisapp_hw10/refs/heads/main/GDMScatalog.csv"
            m = leafmap.Map(center=[23.5, 121], zoom=7)
            m.add_basemap(basemap)
            m.add_heatmap(
                filepath,
                latitude="lat",
                longitude="lon",
                value="ML",
                name="Heat map",
                radius=20,
                opacity=0.5,
            )
    m.to_streamlit(height=700)
