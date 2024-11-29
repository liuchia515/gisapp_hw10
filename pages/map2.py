import pandas as pd
import pydeck as pdk
import streamlit as st
import geopandas as gpd

st.set_page_config(layout="wide")
st.title("🗺️map2")

@st.cache_resource
def load_data():
    url = "https://raw.githubusercontent.com/liuchia515/gisapp_hw10/main/difference_result.geojson"
    data = gpd.read_file(url)
    data["elevation"] = data["difference"] * 50
    data["color"] = data["color"].apply(lambda x: [255, 0, 0] if pd.isna(x) else x)
    return data

def map_3d(data, zoom):
    geojson_data = data.to_json()

    st.write(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v10",
            initial_view_state={
                "latitude": data.geometry.centroid.y.mean(),
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
                    get_elevation="elevation",
                    opacity=0.8,
                ),
            ],
        )
    )

data = load_data()
st.title("3D GeoJSON 地圖展示")
map_3d(data, zoom=7)
