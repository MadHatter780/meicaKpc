import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Set up the Streamlit page
st.set_page_config(layout="wide")

st.markdown("""
    <style>
    
      [data-testid="stMarkdownContainer"] > p {
          font-size: 20px;
          color: white !important;
        }
    </style>
    """, unsafe_allow_html=True)
# Urutan yang diinginkan
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
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
""", unsafe_allow_html=True)
st.markdown("""
    <style>
        /* Background aplikasi */
        [data-testid="stAppViewContainer"] {
            background-color: #f0f0f0;
        }
        
   
        
                
          span {
             color:white !important;
             padding: 10px;
             font-size : 20px;
         }
          .main {
            padding-top: 0px !important;
        }
        .block-container {
            padding-top: 0px !important;
        }
        h1 {
            margin-top: 0px !important;
        }
       
         [data-testid="stMain"]{
        display: flex;
        
        background-image: url("https://frppaneltank.com/wp-content/uploads/2021/10/Conveyor-2.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        
    }
     div[data-testid="stSidebarContent"]{
             background-color:black;
             
         }
    .st-emotion-cache-12fmjuu{
        display:none !important;
    }
    
     .stHeader {
            display: flex;
            justify-content: center; /* Menyebar elemen di kiri dan kanan */
            align-items: center;            /* Menyelaraskan elemen secara vertikal */
            background-color: rgba(0,0,0,0.5);      /* Warna latar belakang */
            color: white;                   /* Warna teks */
            padding: 10px 20px;             /* Padding atas/bawah dan kiri/kanan */
            border-radius: 5px;             /* Sudut membulat */
        }
        .stHeader .header-text {
            padding:5px 10px;
            background-color:black;
            font-size: 1.5em;               /* Ukuran font */
            border-radius:10px;
        }
        .stHeader .header-icon {
            font-size: 1.8em;               /* Ukuran font untuk ikon atau elemen lainnya */
        }


        .header {
            color: white;
            text-align: center;
            padding-bottom: 10px;
            font-size: 22px;
            font-weight: bold;
        }
       
        
        .table {
            width: 100%;
            border-collapse: separate;
            margin-top: 10px;
                border-spacing: 10px 10px;    /* Margin vertikal 10px */

        }

        .table th, .table td {
            border: 1px solid rgba(255, 255, 255, 0.5);
            padding: 8px;
            text-align: center;
            font-size: 14px;
            color: white;
        }

        .table th {
            background-color: rgba(255, 255, 255, 0.2);
        }

        .status-run {
            margin:0px 10px;
            color: green !important;
            background-color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-weight: bold;
        }

        .status-stop {
            margin:0px 10px;
            color: red;
            background-color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-weight: bold;
        }
         .status-isi {
            margin:0px 10px;
            color: black !important;
            background-color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-weight: bold;
        }

        .info-row {
            background-color: rgba(255, 255, 255, 0.2);
            font-weight: bold;
        }
        
    div[data-testid="stHorizontalBlock"] {
            border-radius: 10px;
            padding: 20px;
            color: white;
        }

.st-emotion-cache-1wmy9hl .e1f1d6gn1 > div[data-testid="stVerticalBlock"] .st-emotion-cache-bmmsbz .e1f1d6gn2 > 

    st-emotion-cache-keje6w.e1f1d6gn3 {
        width: calc(50% - 1rem);
        flex: 1 1 calc(50% - 1rem);
        display: flex;
        justify-items: center;
        align-items: center;
        }
        
div[data-testid="stHorizontalBlock"] > .st-emotion-cache-keje6w.e1f1d6gn3 div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
    color: white;
    border-radius: 10px;
    padding: 20px;
    
  
}

.st-emotion-cache-12x0zl8 .e1f1d6gn2 {
    gap: -1rem !important;
}

.st-emotion-cache-1r6slb0{
    background-color:rgba(0,0,0,0.5);
    padding:20px;
    border-radius:10px;
}

div[data-testid="stButton"]{
    display:flex;
    justify-content:center;
}

p{
    color:white;
}
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title-style text-5xl font-semibold">GENERATE CSV</h1>', unsafe_allow_html=True)
# Menampilkan Plot di Streamlit
# Membuat dataset statis (langsung digunakan tanpa dropdown)
data = pd.DataFrame({
    'X': [1, 2, 3, 4],
    'Y1': [10, 15, 7, 20],
    'Y2': [30, 10, 15, 25],
    'Y3': [5, 25, 10, 30],
    'Y4': [20, 5, 25, 15],
})

datasets = {
    "Dataset 1": pd.DataFrame({
        'X': [1, 2, 3, 4],
        'Y1': [10, 15, 7, 20],
        'Y2': [30, 10, 15, 25],
        'Y3': [5, 25, 10, 30],
        'Y4': [20, 5, 25, 15],
    }),
    "Dataset 2": pd.DataFrame({
        'X': [1, 2, 3, 4],
        'Y1': [15, 18, 10, 25],
        'Y2': [20, 30, 25, 35],
        'Y3': [3, 13, 8, 18],
        'Y4': [17, 8, 27, 22],
    }),
    "Dataset 3": pd.DataFrame({
        'X': [1, 2, 3, 4],
        'Y1': [5, 7, 3, 9],
        'Y2': [12, 14, 10, 20],
        'Y3': [8, 10, 12, 15],
        'Y4': [4, 8, 6, 10],
    }),
}
# Membuat grafik Plotly dengan 4 sumbu Y
fig = go.Figure()

# Menambahkan data ke grafik
fig.add_trace(go.Scatter(x=data['X'], y=data['Y1'], name="Y1 Data", yaxis="y1"))
fig.add_trace(go.Scatter(x=data['X'], y=data['Y2'], name="Y2 Data", yaxis="y2"))
fig.add_trace(go.Scatter(x=data['X'], y=data['Y3'], name="Y3 Data", yaxis="y3"))
fig.add_trace(go.Scatter(x=data['X'], y=data['Y4'], name="Y4 Data", yaxis="y4"))

# Konfigurasi layout dengan 4 sumbu Y
fig.update_layout(
    xaxis=dict(title="X Axis", title_font=dict(color='white'), tickfont=dict(color='white')),
    yaxis=dict(title="Y1 (Kiri Utama)", side="left", title_font=dict(color='white'), tickfont=dict(color='white')),
    yaxis2=dict(title="Y2 (Kanan Utama)", overlaying="y", side="right", title_font=dict(color='white'), tickfont=dict(color='white')),
    yaxis3=dict(title="Y3 (Kiri Sekunder)", anchor="free", overlaying="y", side="left", position=0.1, title_font=dict(color='white'), tickfont=dict(color='white')),
    yaxis4=dict(title="Y4 (Kanan Sekunder)", anchor="free", overlaying="y", side="right", position=0.95, title_font=dict(color='white'), tickfont=dict(color='white')),
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    legend=dict(font=dict(color='white'))
)

# Menampilkan grafik di Streamlit tanpa menggunakan dropdown
with st.container():
    col12, col22, col33 = st.columns(3)
    
    # Kolom 1
    with col12:
        st.markdown('<div class="title-style mt-2 mb-4 rounded-xl bg-opacity-0.2 text-3xl bg-black flex text-white justify-center font-bold p-4">SHIFT</div>', unsafe_allow_html=True)
        st.selectbox("Pilih Dataset", options=list(datasets.keys()), key="nested_selectbox_122")
        st.selectbox("Pilih Dataset", options=list(datasets.keys()), key="nested_selectbox_1222")
        st.selectbox("Pilih Dataset", options=list(datasets.keys()), key="nested_selectbox_12211")
        st.selectbox("Pilih Dataset", options=list(datasets.keys()), key="nested_selectbox_2assa")
        st.button("Generate", type="primary", key="generate_button_1")
    
    # Kolom 2
    with col22:
        st.markdown('<div class="title-style mt-2 mb-4 rounded-xl bg-opacity-0.2 text-3xl bg-black flex text-white justify-center font-bold p-4">Trending</div>', unsafe_allow_html=True)
        st.selectbox("Pilih Dataset", options=list(datasets.keys()), key="nested_selectbox_212")
        st.selectbox("Pilih Dataset", options=list(datasets.keys()), key="nested_selectbox_2222")
        st.selectbox("Pilih Dataset", options=list(datasets.keys()), key="nested_selectbox_22211")
        st.selectbox("Pilih Dataset", options=list(datasets.keys()), key="nested_selectbox_22assa")
        st.button("Generate", type="primary", key="generate_button_2")
    
    # Kolom 3
    with col33:
        st.markdown('<div class="title-style mt-2 mb-4 rounded-xl bg-opacity-0.2 text-3xl bg-black flex text-white justify-center font-bold p-4">Trending</div>', unsafe_allow_html=True)
        st.selectbox("Pilih Dataset", options=list(datasets.keys()), key="nested_selectbox_312")
        st.selectbox("Pilih Dataset", options=list(datasets.keys()), key="nested_selectbox_3222")
        st.button("Generate", type="primary", key="generate_button_3")

                         
  