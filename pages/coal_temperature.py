import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(layout="wide")
st.header("COAL TERMINAL-COAL TEMPERATURE")


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
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

hide_top_bar_css = """
    <style>
  div[data-testid="stSidebarContent"]{
             background-color:black !important;
             
         }
          span {
             color:white !important;
             padding: 10px;
             font-size : 20px;
         }
    [data-testid="stHeader"] {
        display: none !important;
    }
    
  
   

   
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

    </style>
    """
st.markdown(hide_top_bar_css, unsafe_allow_html=True)


def barge(title):
    st.markdown(f"""
    <div class="card">
    <div  style="
            display: flex;
            justify-content: center;
            align-items: center;
        ">
       
    </div>
        <table class="table">
            <tbody >
                <tr style="padding:10px; ">
                    <td class="lol">CV-03</td>
                    <td class="status-run lol">RUN</td>
                </tr>
                <tr style="padding:10px;">
                    <td class="lol">CV-04</td>
                    <td class="status-run lol">30 DEG</td>
                </tr>
               <tr style="padding:10px;">
                    <td class="lol">OLC COAL</td>
                    <td class="status-run lol">30 DEG</td>
                </tr>
                <tr class="info-row">
                    <td class="lol">STACKER TRANSFER COAL</td>
                    <td colspan="2" class="status-run LOL">30%</td>
                </tr>
                <tr style="padding:10px;">
                    <td class="lol">SOUTH TRANSFER COAL</td>
                    <td class="status-run lol">30 DEG</td>
                </tr>
                   <tr style="padding:10px;">
                    <td class="lol">NORTH TRANSFER COAL</td>
                    <td class="status-run lol">30 DEG</td>
                </tr>
                 </tr>
                   <tr style="padding:10px;">
                    <td class="lol">BLF COAL</td>
                    <td class="status-run lol">30 DEG</td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)


def cpp_1_rr(val1,val2):
   st.markdown(f"""
    <div class="card">
    <div  style="
            display: flex;
            justify-content: center;
            align-items: center;
        ">
        <div class="text-xl font-semibold bg-black p-3 text-white rounded-b-lg -mt-5">CPP-1 CRUSHING RATE</div>
    </div>
    <div class="w-full flex flex-col gap-y-3">
    
    <div class="w-full flex items-center">
            <div class="w-3/4 text-white text-xl font-semibold">
            </div>
            <div class="w-1/4 px-4 flex text-white justify-center py-2">
                TPH
            </div>
       </div>
    
       <div class="w-full flex items-center">
            <div class="w-3/4 text-white text-xl font-semibold">
                CV-03   
            </div>
            <div class="w-1/4 px-4 rounded-lg bg-white py-2">
                asas
            </div>
       </div>
       
       <div class="w-full flex items-center">
            <div class="w-3/4 text-white text-xl font-semibold">
                STOCKPILE-2
            </div>
            <div class="w-1/4 px-4 rounded-lg bg-white py-2">
                asas
            </div>
       </div>
       
       <div class="w-full flex items-center">
            <div class="w-3/4 text-white text-xl font-semibold">
                STOCKPILE-3
            </div>
            <div class="w-1/4 px-4 rounded-lg bg-white py-2">
                asas
            </div>
       </div>
       
       <div class="w-full flex items-center">
            <div class="w-3/4 text-white text-xl font-semibold">
                PRODUCT RECLAIM CONVEYOR
            </div>
            <div class="w-1/4 px-4 rounded-lg bg-white py-2">
                asas
            </div>
       </div>
    </div>
    </div>
    """, unsafe_allow_html=True)


col1,col2 = st.columns(2)
with col2:
    cpp_1_rr("asas","Asa")