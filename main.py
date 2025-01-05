import streamlit as st
from pages import page1, page2

# Membuat sidebar menu
st.sidebar.title("Menu")
page = st.sidebar.selectbox("Pilih halaman", ["Halaman 1", "Halaman 2"])

st.markdown(hide_top_bar_css, unsafe_allow_html=True)

# Menampilkan halaman berdasarkan pilihan di sidebar
if page == "Halaman 1":
    page1.app()
elif page == "Halaman 2":
    page2.app()
