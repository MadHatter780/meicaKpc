import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Konfigurasi halaman
st.set_page_config(layout="wide")
st.header("COAL TERMINAL-TRENDING")

# Dataframe dengan data acak
chart_data = pd.DataFrame({
    "col1": np.random.randn(20),
    "col2": np.random.randn(20),
    "col3": np.random.choice(["A", "B", "C", "D"], 20),
})

# Membuat grafik dengan Altair
chart = alt.Chart(chart_data).mark_line().encode(
    x="col1",
    y="col2",
    color="col3"
).properties(
    width=800,
    height=400,
    background="#000000"  # Latar belakang hitam
).configure_axis(
    gridColor="#444",
    labelColor="#FFFFFF",
    titleColor="#FFFFFF"
).configure_legend(
    labelColor="#FFFFFF",
    titleColor="#FFFFFF"
).configure_view(
    strokeWidth=0
)

# Menampilkan grafik di Streamlit
st.altair_chart(chart, use_container_width=True)
