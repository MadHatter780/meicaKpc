import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(layout="wide")

# CSS diperbarui untuk memperbesar teks isi dan tetap menjaga tata letak
st.markdown("""
    <style>
    /* Wallpaper tetap dengan overlay */
    [data-testid="stAppViewContainer"] > .main {
        display: flex;
        justify-content: center;
        align-items: center;
        background-image: url("https://frppaneltank.com/wp-content/uploads/2021/10/Conveyor-2.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        padding: 20px;
    }

    /* Judul kotak dengan border yang menyesuaikan teks dan posisi tengah */
    .title-box {
        padding: 5px 15px;
        border-radius: 10px;
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        display: inline-block;
        border-width: 2px;
        margin: 0 auto;
        background-color: #000;
    }

    /* Border untuk Actual Updated dan Capacity dengan warna masing-masing */
    .actual-title {
        border: 2px solid green;
        color: green;
    }

    .capacity-title {
        border: 2px solid blue;
        color: blue;
    }

    /* Styling untuk isi konten dengan font lebih besar */
    .info-box {
        background-color: rgba(0, 0, 0, 0.7); 
        padding: 20px;
        border-radius: 15px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.5);
        color: white;
        text-align: center;
    }

    /* Ukuran teks isi diperbesar */
    .content-text {
        font-size: 28px;  /* Ukuran teks isi diperbesar di sini */
        color: white;
        font-weight: bold;
        background-color : #000;
        padding : 0px 10px 0px 10px;
        width: 90%;
        margin-top:10px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Header Title
st.markdown('<h1 class="title-style">Coal Terminal-Vessel Status</h1>', unsafe_allow_html=True)

# Container untuk informasi vessel dan target
with st.container(border=True):
    col1, col2 = st.columns(2)
    
    # Vessel Information
    with col1:
        with stylable_container(key="vessel_info", css_styles=["{background-color: rgba(0, 0, 0, 0.7); padding: 20px; border-radius: 15px;}"]):
            st.markdown("""
                <p class="content-text"><b>VESSEL NAME:</b> CARALOS GLORY</p>
                <p class="content-text"><b>COMMENCE DATE:</b> 03 March 2024</p>
                <p class="content-text"><b>COMMENCE TIME:</b> 11:00:20</p>
            """, unsafe_allow_html=True)

    # Target Information
    

# Container untuk Actual Updated dan Capacity dengan border sesuai teks
with st.container(border=True):
    col1, col2 = st.columns(2)
    
    # Actual Updated dengan judul yang center dan border hijau
    with col1:
        with stylable_container(key="actual_info", css_styles=["{background-color: rgba(0, 0, 0, 0.7); padding: 20px; border-radius: 15px;}"]):
            st.markdown('<p class="title-box actual-title">Actual Updated</p>', unsafe_allow_html=True)
            st.markdown("""
                <p class="content-text"><b>AVG LOADING RATE:</b> 4,200 TPH</p>
                <p class="content-text"><b>EST. COMPLETION DATE:</b> 06 March 2024</p>
                <p class="content-text"><b>EST. COMPLETION TIME:</b> 08:00:50</p>
            """, unsafe_allow_html=True)
    with col2:
        with stylable_container(key="target_info", css_styles=["{background-color: rgba(0, 0, 0, 0.7); padding: 20px; border-radius: 15px;}"]):
            st.markdown('<p class="title-box" style="border: 2px solid red; color: red;">Target</p>', unsafe_allow_html=True)
            st.markdown("""
                <p class="content-text"><b>LOADING RATE:</b> 5,200 TPH</p>
                <p class="content-text"><b>COMPLETION DATE:</b> 05 March 2024</p>
                <p class="content-text"><b>COMPLETION TIME:</b> 16:00:11</p>
            """, unsafe_allow_html=True)

    # Capacity dengan judul yang center dan border biru
        
