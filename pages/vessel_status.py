import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(layout="wide")
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none !important;
        }
        [data-testid="stSidebar"]
    </style>
    """, unsafe_allow_html=True)
if "sidebar_items" not in st.session_state:
    st.session_state.sidebar_items = [
        "Vessel Status",
        "Conveyor Status",
        "Coal Temperature",
        "Trending",
        "Generate CSV"
    ]
for item in st.session_state.sidebar_items:
    file_name = item.lower().replace(" ", "_") + ".py"
    st.sidebar.page_link(f"pages/{file_name}", label=item)


st.markdown("""
    <style>
    /* Wallpaper tetap dengan overlay */
    [data-testid="stMain"]  {
        display: flex;
        justify-content: center;
        align-items: center;
        background-image: url("https://frppaneltank.com/wp-content/uploads/2021/10/Conveyor-2.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        padding: 20px;
    }

   
    .st-emotion-cache-12fmjuu{
        display:none !important;
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
     div[data-testid="stSidebarContent"]{
             background-color:black !important;
             
         }
          span {
             color:white !important;
             padding: 10px;
             font-size : 20px;
         }

    /* Ukuran teks isi diperbesar */
    
     ul {
    display: flex;
    flex-direction: column; /* Tetap mengatur urutan kolom dari atas ke bawah */
    list-style-type: none;
    padding: 0;
}
    li:nth-child(1) {
        order: 5; /* Menempatkan elemen pertama di urutan kelima */
    }
    li:nth-child(2) {
        order: 2; /* Menempatkan elemen kedua di urutan kedua */
    }
    li:nth-child(3) {
        order: 3; /* Menempatkan elemen ketiga di urutan ketiga */
    }
    li:nth-child(4) {
        order: 4; /* Menempatkan elemen keempat di urutan keempat */
    }
    li:nth-child(5) {
        order: 1; /* Menempatkan elemen kelima di urutan pertama */
    }

    
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
    st.markdown('''
    <div class="bg-black w-full" 
         style="width:100%; 
                display:flex; 
                justify-content: space-between;  
                background-color:black; 
                padding:10px;">
        <div style="color:white;font-size:30px;">Total Capacity : 70.000 TONNESE</div>
        <div style="color:white;font-size:30px;">Total Loaded : 70.000 TONNESE</div>
        <div style="color:white;font-size:30px;">Remaining To Load : 70.000 TONNESE</div>

    </div>
''', unsafe_allow_html=True)    
    # Capacity dengan judul yang center dan border biru
        
