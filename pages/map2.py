import pandas as pd
import pydeck as pdk
import streamlit as st

st.set_page_config(layout="wide")
st.title("🗺️map2")

@st.cache_resource
def load_data():
    url = "https://raw.githubusercontent.com/liuchia515/gisapp_hw10/main/difference_result.geojson"
    data = pd.read_json(url)  # 讀取 GeoJSON 文件
    return data

def map_3d(data, zoom):
    st.write(
        pdk.Deck(
            map_style=None,
            initial_view_state={
                "latitude": data["geometry"]["coordinates"][0][1],
                "longitude": data["geometry"]["coordinates"][0][0],
                "zoom": zoom,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "GeoJsonLayer",
                    data=data,
                    pickable=True,
                    stroked=False,
                    filled=True,
                    extruded=True,
                    get_fill_color="[255, 0, 0, 140]",
                    get_line_color="[0, 0, 0, 140]",
                    get_elevation="properties.elevation",
                ),
            ],
        )
    )

data = load_data()
st.title("3D GeoJSON 地圖展示")
map_3d(data, zoom=7)
