import streamlit as st
import plotly.graph_objects as go
import numpy as np
import json
import psycopg2
import pandas as pd



DB_NAME = "streamlit"
DB_USER = "postgres"
DB_PASSWORD = "helloworld"
DB_HOST = "localhost"  # atau IP server PostgreSQL
DB_PORT = "5432"

def get_all_data_as_json():
    try:
        # Membuka koneksi ke database
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        
        # Mengambil metadata kolom dengan query
        query = "SELECT * FROM ct_conveyor_status LIMIT 0;"  # Mengambil 0 baris, hanya metadata kolom
        df = pd.read_sql_query(query, conn)
        
        # Menutup koneksi
        conn.close()
        
        # Mengambil nama kolom
        column_names = df.columns.tolist()

        # Konversi nama kolom menjadi JSON
        data_json = json.dumps({"columns": column_names})
        
        return data_json
    except Exception as e:
        return json.dumps({"error": str(e)})
# Tampilan di Streamlit
data_json = get_all_data_as_json()


st.set_page_config(layout="wide")
st.title("Multiple Y-Axis Example with Range Slider and Dynamic Selectbox")

st.write(data_json)

# Fungsi untuk membuat data acak
def generate_random_data():
    return np.random.randint(1, 10, size=100).tolist()

data_options = {
    "Random Data 1": generate_random_data(),
    "Random Data 2": generate_random_data(),
    "Random Data 3": generate_random_data(),
    "Random Data 4": generate_random_data()
}


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
       
         [data-testid="stAppViewContainer"] > .main {
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


st.markdown("### Select Data for Each Y-Axis")

st.markdown("### Select Data for Each Y-Axis")
col12, col22 = st.columns(2)

# **Memilih data langsung dengan selectbox tanpa tombol toggle**
with col12:
    y1_data = st.selectbox("Select Y1 Data", list(data_options.keys()), index=0)
    st.write(f"**Y1 Selected:** {y1_data}")

with col22:
    y2_data = st.selectbox("Select Y2 Data", list(data_options.keys()), index=1)
    st.write(f"**Y2 Selected:** {y2_data}")



col1, col2, col3, col4 = st.columns(4)

# **Memilih data langsung dengan selectbox tanpa tombol toggle**
with col1:
    y1_data = st.selectbox("Select Y1 Data", list(data_options.keys()), index=2)
    st.write(f"**Y1 Selected:** {y1_data}")

with col2:
    y2_data = st.selectbox("Select Y2 Data", list(data_options.keys()), index=3)
    st.write(f"**Y2 Selected:** {y2_data}")

with col3:
    y3_data = st.selectbox("Select Y3 Data", list(data_options.keys()), index=3)
    st.write(f"**Y3 Selected:** {y3_data}")

with col4:
    y4_data = st.selectbox("Select Y4 Data", list(data_options.keys()), index=3)
    st.write(f"**Y4 Selected:** {y4_data}")

fig = go.Figure()

# Menambahkan data sesuai pilihan terbaru di selectbox
fig.add_trace(go.Scatter(
    x=list(range(1, 101)),
    y=data_options[y1_data],
    name="Y1 Data"
))

fig.add_trace(go.Scatter(
    x=list(range(1, 101)),
    y=data_options[y2_data],
    name="Y2 Data",
    yaxis="y2"
))

fig.add_trace(go.Scatter(
    x=list(range(1, 101)),
    y=data_options[y3_data],
    name="Y3 Data",
    yaxis="y3"
))

fig.add_trace(go.Scatter(
    x=list(range(1, 101)),
    y=data_options[y4_data],
    name="Y4 Data",
    yaxis="y4"
))

# Konfigurasi layout dengan Range Slider
fig.update_layout(
    xaxis=dict(
        domain=[0.2, 0.8],
        rangeslider=dict(visible=True),
        type="linear"
    ),
    yaxis=dict(title="yaxis1"),
    yaxis2=dict(title="yaxis2", overlaying="y", side="left", position=0.1),
    yaxis3=dict(title="yaxis3", overlaying="y", side="right"),
    yaxis4=dict(title="yaxis4", overlaying="y", side="right", position=0.9),
    title_text="Multiple Y-Axis with Dynamic Data Selection",
    width=900,
    height=600,
    showlegend=True
)

# Menampilkan grafik dengan data yang diperbarui langsung
st.plotly_chart(fig, use_container_width=True)
