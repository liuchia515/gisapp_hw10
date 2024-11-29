import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(layout="wide")
st.title("🗺️map3")
url = "https://raw.githubusercontent.com/liuchia515/gisapp_hw10/main/difference_result.geojson"
data=gpd.read_file(url)

def map_3d(data,zoom):
    geojson = data.to_json
    st.write(
        pdk.Deck(
            map_style=None,
            initial_view_stste={
                "latitude":data.geometry.centroid.y.mean(),
                "longitude": data.geometry.centroid.x.mean(),
                "zoom": zoom,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "GeoJsonLayer",
                    data=geojson_data,
                    pickable=True,
                    stroked=False,
                    filled=True,
                    extruded=True,
                    get_fill_color=["get", "color"],
                    get_elevation="difference",
                    opacity=0.8,
                ),
            ],
        )
    )
st.title("3D GeoJSON 地圖展示")
map_3d(data, zoom=7)
