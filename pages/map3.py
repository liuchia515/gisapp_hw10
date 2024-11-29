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
    
    try:
        data = gpd.read_file(url)
        
        # 顯示資料的基本信息
        st.write("GeoDataFrame Info:")
        st.write(data.info())
        
        # 顯示資料的前幾行
        st.write("GeoDataFrame 前幾行:")
        st.write(data.head())

        # 檢查幾何列資料
        st.write("幾何列資料:")
        st.write(data.geometry.head())
        
        # 檢查幾何資料是否有效
        st.write("幾何資料是否有效:")
        st.write(data.geometry.is_valid.sum())
        
        # 檢查是否有缺失值
        st.write("檢查是否有缺失值:")
        st.write(data.isnull().sum())

        # 顯示差異(difference)欄位的統計資訊
        st.write("Difference 欄位的統計資訊:")
        st.write(data['difference'].describe())

        # 顯示顏色(color)欄位的統計資訊
        st.write("Color 欄位的統計資訊:")
        st.write(data['color'].describe())

        # 轉換顏色欄位為RGB格式
        def hex_to_rgb(hex_color):
            return mcolors.hex2color(hex_color)

        data['rgb_color'] = data['color'].apply(hex_to_rgb)
        
        # 顯示 rgb_color 欄位的前幾行
        st.write("RGB 顏色的前幾行:")
        st.write(data[['color', 'rgb_color']].head())

        # 清理無效幾何資料
        data = data[data.geometry.is_valid]
        data = data.dropna(subset=["geometry"])

        return data
    
    except Exception as e:
        st.write("加載 GeoJSON 數據時出錯:", e)

def map_3d(data, zoom):
    geojson = data.to_json()
    map_style = "mapbox://styles/mapbox/light-v10"  # 更改為有效的 Mapbox 樣式

    st.write(
        pdk.Deck(
            map_style=map_style,
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
if data is not None:
    st.title("3D GeoJSON 地圖展示")
    map_3d(data, zoom=7)  # 呼叫 map_3d 函數並傳遞數據和縮放參數
else:
    st.write("未能成功加載資料，請檢查 GeoJSON 文件或網絡連接。")
