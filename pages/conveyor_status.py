import streamlit as st
import psycopg2
import pandas as pd
import json
from streamlit_autorefresh import st_autorefresh

# Konfigurasi layout penuh
st.set_page_config(layout="wide")


DB_NAME = "streamlit"
DB_USER = "postgres"
DB_PASSWORD = "helloworld"
DB_HOST = "localhost"  # atau IP server PostgreSQL
DB_PORT = "5432"


st_autorefresh(interval=2000)

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


def get_all_data_as_json():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        query = "SELECT * FROM ct_conveyor_status ORDER BY created_at DESC LIMIT 1;"
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        # Konversi DataFrame menjadi JSON
        data_json = df.to_json(orient="records")  # Menggunakan orientasi records untuk format array JSON
        return data_json
    except Exception as e:
        return json.dumps({"error": str(e)})

# Tampilan di Streamlit
data_json = get_all_data_as_json()
lol = json.loads(data_json)[0]

# CSS untuk efek glassmorphism pada card
st.markdown("""
    <style>
        /* Background aplikasi */
        [data-testid="stAppViewContainer"] {
            background-color: #f0f0f0;
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

        /* Card styling dengan efek kaca */
        .card {
            margin-top:10px;
            background: rgba(0, 0, 0, 0.7); /* Hitam dengan transparansi */
            padding: 20px;
            backdrop-filter: blur(10px); /* Efek kaca */
            -webkit-backdrop-filter: blur(10px);
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
            margin-bottom: 20px;
            border-radius:20px;
        }

        .header {
            color: white;
            text-align: center;
            padding-bottom: 10px;
            font-size: 22px;
            font-weight: bold;
        }
        .st-emotion-cache-1wmy9hl > .st-emotion-cache-115gedg{
            background-color:rgba(0, 0, 0, 0.5); padding:10px;border-radius:10px;

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
        div[data-testid="stVerticalBlockBorderWrapper"] > .e1f1d6gn1 > .e1f1d6gn2 >.e1f1d6gn5 div[data-testid="stHorizontalBlock"] {
            background-color: rgba(0,0,0,0.5); /* Warna latar belakang */
            border-radius: 0px 0px 0px 0px;
            padding: 20px;
            color: white;
        }
         div[data-testid="stSidebarContent"]{
             background-color:black !important;
             
         }
          span {
             color:white !important;
             padding: 10px;
             font-size : 20px;
         }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title-style">Coal Terminal-Conveyor Status</h1>', unsafe_allow_html=True)


def stream_1(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12):
    st.markdown(f"""
    <div class="card">
    <div  style="
            display: flex;
            justify-content: center;
            align-items: center;
        ">
        <h4 style="
            display: inline-block;
            color: white;
            padding: 10px 10px;
            background-color: #000;
            border-radius: 8px;
            letter-spacing: 3px;">STREAM 1</h4>
    </div>
        <table class="table">
            <thead>
                <tr>
                    <th>Unit</th>
                    <th>STATUS</th>
                    <th>TPH</th>
                </tr>
            </thead>
            <tbody>
                <tr style="padding:10px;">
                    <td>CV05</td>
                    <td class="status-run">{val1}</td>
                    <td class="status-isi">{val2}</td>
                </tr>
                <tr style="padding:10px;">
                    <td>CV07</td>
                    <td class="status-run">{val3}</td>
                    <td class="status-isi">{val4}</td>
                </tr>
               <tr style="padding:10px;">
                    <td>OLC-1</td>
                    <td class="status-run">{val5}</td>
                    <td class="status-isi">{val6}</td>
                </tr>
             <tr style="padding:10px;">
                    <td>STACKING</td>
                    <td class="status-run">{val7}</td>
                    <td class="status-isi">{val8}</td>
                </tr>
             <tr style="padding:10px;">
                    <td>RECLAIMING</td>
                    <td class="status-run">{val9}</td>
                    <td class="status-isi">{val10}</td>
                </tr>
            <tr style="padding:10px;">
                    <td>STACKING2</td>
                    <td class="status-run">{val11}</td>
                    <td class="status-isi">{val12}</td>
                </tr>
                <tr class="info-row">
                    <td>COAL QUALITY</td>
                    <td colspan="2">MELAWAN</td>
                </tr>
                <tr class="info-row">
                    <td>DESTINATION</td>
                    <td colspan="2">PORT</td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)
    

def stream_2(val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12, val13, val14,val15):
    st.markdown(f"""
    <div class="card">
    <div style="
            display: flex;
            justify-content: center;
            align-items: center;
        ">
        <h4 style="
            display: inline-block;
            color: white;
            padding: 10px 10px;
            background-color: #000;
            border-radius: 8px;
            letter-spacing: 3px;">STREAM 2</h4>
    </div>
        <table class="table">
            <thead>
                <tr>
                    <th>Unit</th>
                    <th>STATUS</th>
                    <th>TPH</th>
                </tr>
            </thead>
            <tbody>
                <tr style="padding:10px;">
                    <td>CV06</td>
                    <td class="status-run">{val1}</td>
                    <td class="status-isi">{val2}</td>
                </tr>
                <tr style="padding:10px;">
                    <td>CV08</td>
                    <td class="status-run">{val3}</td>
                    <td class="status-isi">{val4}</td>
                </tr>
               <tr style="padding:10px;">
                    <td>OLC-2</td>
                    <td class="status-run">{val5}</td>
                    <td class="status-isi">{val6}</td>
                </tr>
             <tr style="padding:10px;">
                    <td>STOCKPILE</td>
                    <td class="status-run">{val7}</td>
                </tr>
             <tr style="padding:10px;">
                    <td>STACKING</td>
                    <td class="status-run">{val8}</td>
                    <td class="status-isi">{val9}</td>
                </tr>
                <tr style="padding:10px;">
                    <td>RECLAIMING</td>
                    <td class="status-run">{val10}</td>
                    <td class="status-isi">{val11}</td>
                </tr>
                <tr style="padding:10px;">
                    <td>MTC</td>
                    <td class="status-run">{val12}</td>
                </tr>
                <tr class="info-row">
                    <td>SURGE BIN LEVEL</td>
                    <td colspan="2">{val13}%</td>
                </tr>
                 <tr style="padding:10px;">
                        <td>BELT FEEDER</td>
                        <td class="status-run">{val14}</td>
                        <td class="status-isi">{val15}</td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)

def ship(val1, val2, val3, val4, val5,val6,val7,val8):
    st.markdown(f"""
    <div class="card">
    <div style="
            display: flex;
            justify-content: center;
            align-items: center;
        ">
        <h4 style="
            display: inline-block;
            color: white;
            padding: 10px 10px;
            background-color: #000;
            border-radius: 8px;
            letter-spacing: 3px;">SHIP LOADING FACILITY</h4>
    </div>
        <table class="table">
            <thead>
                <tr>
                    <th>Unit</th>
                    <th>STATUS</th>
                    <th>TPH</th>
                </tr>
            </thead>
            <tbody>
                <tr style="padding:10px;">
                    <td>TRESTLE</td>
                    <td class="status-run">{val1}</td>
                    <td class="status-isi">{val2}</td>
                </tr>
                <tr style="padding:10px;">
                    <td>SOUTH TC</td>
                    <td class="status-run">{val3}</td>
                    <td class="status-isi">{val4}</td>
                </tr>
               <tr style="padding:10px;">
                    <td>SOUTH SL</td>
                    <td class="status-run">{val5}</td>
                </tr>
                <tr style="padding:10px;">
                    <td>NORTH TC</td>
                    <td class="status-run">{val6}</td>
                    <td class="status-isi">{val7}</td>
                </tr>
               <tr style="padding:10px;">
                    <td>NORTH SL</td>
                    <td class="status-run">{val8}</td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)

def barge(val1, val2, val3, val4, val5,val6):
    st.markdown(f"""
    <div class="card">
    <div style="
            display: flex;
            justify-content: center;
            align-items: center;
        ">
        <h4 style="
            display: inline-block;
            color: white;
            padding: 10px 10px;
            background-color: #000;
            border-radius: 8px;
            letter-spacing: 3px;">BARGE LOADING FACILITY</h4>
    </div>
        <table class="table">
            <thead>
                <tr>
                    <th>Unit</th>
                    <th>STATUS</th>
                    <th>TPH</th>
                </tr>
            </thead>
            <tbody>
                <tr style="padding:10px;">
                    <td>BTC-1</td>
                    <td class="status-run">{val1}</td>
                </tr>
                <tr style="padding:10px;">
                    <td>BTC-2</td>
                    <td class="status-run">{val2}</td>
                </tr>
               <tr style="padding:10px;">
                    <td>BLC</td>
                    <td class="status-isi">{val3}</td>                    
                    <td class="status-run">{val4}</td>
                </tr>
                <tr class="info-row">
                    <td>TOTALIZER</td>
                    <td colspan="2" class="status-run">{val5}</td>
                </tr>
                <tr class="info-row">
                    <td>WIND SPEED</td>
                    <td class="status-run" colspan="2">{val6}</td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)

def bengalon(val1,val2,val3,val4):
    st.markdown(f"""
    <div class="card">
    <div  style="
            display: flex;
            justify-content: center;
            align-items: center;
        ">
        <h4 style="
            display: inline-block;
            color: white;
            padding: 10px 10px;
            background-color: #000;
            border-radius: 8px;
            letter-spacing: 3px;">BARGE LOADING FACILITY</h4>
    </div>
        <table class="table">
            <thead>
                <tr>
                    <th>Unit</th>
                    <th>STATUS</th>
                    <th>TPH</th>
                </tr>
            </thead>
            <tbody>
                <tr style="padding:10px;">
                    <td>CV01-INLOADING</td>
                    <td class="status-run">{val1}</td>
                    <td class="status-run">{val2}</td>
                </tr>
                <tr style="padding:10px;">
                    <td>CV01-INLOADING</td>
                    <td class="status-run">{val3}</td>
                    <td class="status-run">{val4}</td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)

with st.container():
    
    col1, col2 = st.columns([2, 1])  # Proporsi 2:1
    with col1:
        st.markdown("""
                <div class="stHeader">
                    <div class="header-text">SANGATTA</div>
                </div>
            """, unsafe_allow_html=True)
        cola1, cola2 = st.columns(2)
        with cola1: 
            
            with st.container():
                stream_1(lol["s1_cv05_status"],lol["s1_cv05_tph"]
                ,lol["s1_cv07_status"],lol["s1_cv07_tph"]
                ,lol["s1_olc_1_status"],lol["s1_olc_1_tph"]
                ,lol["s1_stacking_status"],lol["s1_stacking_tph"]
                ,lol["s1_reclaiming_status"],lol["s1_reclaiming_tph"]
                ,lol["s1_stacking2_status"],lol["s1_stacking2_tph"]
                )
                stream_2(lol["s2_cv06_status"],lol["s2_cv06_status"]
                ,lol["s2_cv08_status"],lol["s2_cv08_tph"]
                ,lol["s2_olc_2_status"],lol["s2_olc_2_tph"]
                ,lol["s2_stockpile_status"],
                lol["s2_stacking_status"],lol["s2_stacking_tph"]
                ,lol["s2_reclaiming_status"],lol["s2_reclaiming_tph"]
                ,lol["s2_mtc_status"],lol["s2_surge_bin_level"]
                ,lol["s2_belt_feeder_status"],lol["s2_belt_feeder_tph"]
                )
        with cola2:
            with st.container():
                ship(lol["slp_trestle_status"],lol["slp_trestle_tph"]
                ,lol["slp_south_tc_status"],lol["slp_south_tc_tph"]
                ,lol["s1_south_sl_status"],lol["slp_north_tc_status"]
                ,lol["slp_north_tc_tph"],lol["slp_north_sl_status"])
                barge(lol["blf_sangata_btc_1"],lol["blf_sangata_btc_2"]
                ,lol["blf_blc_status"],lol["blf_blc_tph"]
                ,lol["blf_sangata_totalizer"],lol["blf_sangata_wind_speed"])
    with col2:
         with st.container():
            st.markdown("""
                <div class="stHeader">
                    <div class="header-text">BENGALON</div>
                </div>
            """, unsafe_allow_html=True)    
            bengalon(lol["blf_bengalon_cv01_inloading_status"],lol["blf_bengalon_cv01_inloading_tph"]
                ,lol["blf_bengalon_cv05_outlanding_status"],lol["blf_bengalon_cv05_outlanding_tph"])
