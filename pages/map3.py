import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

url = "https://raw.githubusercontent.com/liuchia515/gisapp_hw10/main/difference_result.geojson"
chart_data = pd.DataFrame(url)

st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=chart_data,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
        ],
    )
)
