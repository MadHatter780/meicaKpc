import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.add_vertical_space import add_vertical_space

# Konfigurasi halaman Streamlit
st.set_page_config(layout="wide")
st.header("COAL TERMINAL-TRENDING")

# Menyembunyikan top bar dan mengatur latar belakang
hide_top_bar_css = """
    <style>
    [data-testid="stHeader"] {
        display: none !important;
    }
    [data-testid="stVerticalBlockBorderWrapper"]{
        background-color: rgba(0, 0, 0, 0.5);
        border-radius:10px;
    }
    [data-testid="stHorizontalBlock"]{
        padding-top:40px;
    }
    [data-testid="stAppViewContainer"] > .main {
        color:white;
        background-image: url("https://frppaneltank.com/wp-content/uploads/2021/10/Conveyor-2.jpg");
        background-repeat: no-repeat;
        background-attachment: local;
    }
    </style>
"""
st.markdown(hide_top_bar_css, unsafe_allow_html=True)

# Membuat data untuk grafik
chart_data = pd.DataFrame(
    {
        "col1": np.random.randn(20),
        "col2": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C", "D"], 20),
    }
)

# Menggunakan Plotly Express untuk membuat grafik dengan tema gelap
fig = px.line(chart_data, x="col1", y="col2", color="col3", template="plotly_dark")

# Menampilkan grafik
st.plotly_chart(fig)

# Kontainer yang dapat di-stylable
with stylable_container(
    key="cat_container1",
    css_styles=[
        """
        {
            background-color: #212f3c;
            padding: 0.5em;
            border-radius: 5em;
        }
        """,
        """
        .stMarkdown {
            padding-right: 1.5em;
        }
        """
    ],
):
    col1, col2, col3, col4 = st.columns([10, 20, 20, 10])
    with col2:
        with st.container():
            col2_1, col2_2, col2_3, col2_4 = st.columns([7, 8, 8, 7])
            with col2_2:
                add_vertical_space(4)
                st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">START DATE:</p>', unsafe_allow_html=True)
                add_vertical_space(1)
                st.markdown(f'<p style="margin-bottom:100px;text-align:left;font-size:20px;border-radius:2%;">END DATE:</p>', unsafe_allow_html=True)
            with col2_3:
                add_vertical_space(4)
                option2 = st.selectbox('', ('Option 1', 'Option 2', 'Option 3'), key="option12", label_visibility="collapsed")
                option3 = st.selectbox('', ('Option 1', 'Option 2', 'Option 3'), key="option13", label_visibility="collapsed")
    with col3:
        with st.container():
            col3_1, col3_2, col3_3, col3_4 = st.columns([4, 11, 11, 4])
            with col3_2:
                st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">SHIFT REPORTING:</p>', unsafe_allow_html=True)
                add_vertical_space(1)
                st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">DATE:</p>', unsafe_allow_html=True)
                add_vertical_space(1)
                st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">TIME:</p>', unsafe_allow_html=True)
                add_vertical_space(1)
                st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">PATH DIRECTORY:</p>', unsafe_allow_html=True)
            with col3_3:
                option1 = st.selectbox('', ('Option 1', 'Option 2', 'Option 3'), key="option21", label_visibility="collapsed")
                option2 = st.selectbox('', ('Option 1', 'Option 2', 'Option 3'), key="option22", label_visibility="collapsed")
                option3 = st.selectbox('', ('Option 1', 'Option 2', 'Option 3'), key="option23", label_visibility="collapsed")
                option4 = st.selectbox('', ('Option 1', 'Option 2', 'Option 3'), key="option24", label_visibility="collapsed")
