import streamlit as st

st.set_page_config(page_title="Main Page", layout="wide")
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none !important;
        }
    </style>
    """, unsafe_allow_html=True)
# Urutan yang diinginkan
if "sidebar_items" not in st.session_state:
    st.session_state.sidebar_items = [
        "Vessel Status",
        "Conveyor Status",
        "Coal Temperature",
        "Trending",
        "Generate CSV"
    ]


# Tampilkan daftar halaman di sidebar sesuai urutan yang sudah ditentukan
for item in st.session_state.sidebar_items:
    file_name = item.lower().replace(" ", "_") + ".py"
    st.sidebar.page_link(f"pages/{file_name}", label=item)


st.write("Ini adalah halaman utama.")
