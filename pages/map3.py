import streamlit as st
import geopandas as gpd

# 加載資料
@st.cache_resource
def load_data():
    url = "https://raw.githubusercontent.com/liuchia515/gisapp_hw10/main/difference_result.geojson"
    data = gpd.read_file(url)
    
    # 顯示資料基本結構
    st.write("GeoDataFrame Info:")
    st.write(data.info())  # 顯示資料的簡要結構

    # 顯示幾何列資料
    st.write("幾何資料列：")
    st.write(data.geometry.head())

    # 檢查幾何是否有效
    st.write("幾何資料是否有效：")
    st.write(data.geometry.is_valid.sum())  # 顯示有效幾何的數量

    return data

# 渲染資料
data = load_data()


import pydeck as pdk

# 顯示簡單的 2D 地圖
def simple_map(data):
    # 使用 GeoJSON 資料
    geojson = data.to_json()
    
    # 渲染地圖
    st.write(
        pdk.Deck(
            initial_view_state={
                "latitude": data.geometry.centroid.y.mean(),
                "longitude": data.geometry.centroid.x.mean(),
                "zoom": 7,
            },
            layers=[
                pdk.Layer(
                    "GeoJsonLayer",
                    data=geojson,
                    pickable=True,
                    stroked=False,
                    filled=True,
                    get_fill_color=[255, 0, 0],  # 渲染為紅色
                ),
            ],
        )
    )

# 呼叫簡單地圖
simple_map(data)


def map_3d(data, zoom):
    geojson = data.to_json()

    st.write(
        pdk.Deck(
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
                    get_elevation="difference",  # 假設 'difference' 是數值欄位
                    opacity=0.8,
                ),
            ],
        )
    )

map_3d(data, zoom=7)


import matplotlib.colors as mcolors

def hex_to_rgb(hex_color):
    return mcolors.hex2color(hex_color)

data['rgb_color'] = data['color'].apply(hex_to_rgb)
