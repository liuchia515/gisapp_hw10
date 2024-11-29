import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import geopandas as gpd
import matplotlib.colors as mcolors

st.set_page_config(layout="wide")
st.title("🗺️map3")

@st.cache_resource
def load_data():
    url = "https://raw.githubusercontent.com/liuchia515/gisapp_hw10/main/difference_result.geojson"
    data = gpd.read_file(url)
    
    # 顯示資料的基本信息
    st.write("GeoDataFrame Info:")
    st.write(data.info())
    
    # 顯示 difference 欄位的描述
    st.write("Difference 欄位的統計信息:")
    st.write(data['difference'].describe())
    
    # 轉換顏色欄位為RGB格式
    def hex_to_rgb(hex_color):
        return mcolors.hex2color(hex_color)

    data['rgb_color'] = data['color'].apply(hex_to_rgb)
    
    # 顯示 rgb_color 欄位的部分資料
    st.write("RGB 顏色的前幾行:")
    st.write(data[['color', 'rgb_color']].head())

    return data

def map_3d(data, zoom):
    geojson = data.to_json()
    st.write(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v10",  # 更改為有效的 Mapbox 樣式
            initial_view_state={
                "latitude": data.geometry.centroid.y.mean(),
                "longitude": data.geometry.centroid.x.mean(),
                "zoom": zoom,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "GeoJsonLayer",
                    data=geojson,
                    pickable=True,
                    stroked=False,
                    filled=True,
                    extruded=True,
                    get_fill_color=["get", "rgb_color"],
                    get_elevation="difference",
                    opacity=0.8,
                ),
            ],
        )
    )

data = load_data()  # 加載數據
st.title("3D GeoJSON 地圖展示")
map_3d(data, zoom=7)  # 呼叫 map_3d 函數並傳遞數據和縮放參數
