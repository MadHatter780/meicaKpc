import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.add_vertical_space import add_vertical_space
import streamlit_nested_layout


st.set_page_config(layout="wide")
col1,col2 = st.columns([42,21])
hide_top_bar_css = """
    <style>
    p{
        margin : 20px;
    }
    [data-testid="stHeader"] {
        display: none !important;
    }
     [data-testid="stMarkdown"] {
        background-color: white; /* Red with 50% opacity */

    }
    [data-testid="stVerticalBlockBorderWrapper"]{
        background-color: rgba(0, 0, 0, 0.5); /* Red with 50% opacity */
    border-radius:10px;
    }
    [data-testid="stAppViewContainer"] > .main {
    background-image: url("https://frppaneltank.com/wp-content/uploads/2021/10/Conveyor-2.jpg");
    background-repeat: no-repeat;
    background-attachment: local;
}
    </style>
    """
st.markdown(hide_top_bar_css, unsafe_allow_html=True)

with col1:
    with st.container(border=True):
        st.markdown(f'<p style="background-color:black;text-align:center;font-size:24px;border-radius:2%;">SANGATTA</p>', unsafe_allow_html=True)
        col11,col12 = st.columns([21,21])
        with col11:
            with st.container(border=True):
                st.markdown(f'<p style="background-color:black;text-align:center;font-size:20px;border-radius:2%;">STREAM1</p>', unsafe_allow_html=True)
                with st.container():
                    col111,col112,col113 = st.columns([7,7,7])
                    with col111:
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;"></p><br>', unsafe_allow_html=True)
                        st.markdown(f'<p style=text-align:left;font-size:12px;border-radius:2%;">CV05</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;">CV07</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;">OLC-1</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;">STACKING</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;">RECLAIMING</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;">STACKING</p>', unsafe_allow_html=True)
                    with col112:
                        st.write("STATUS")
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">RUN</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;">STOP</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">RUN</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;">STOP</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">RUN</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;">STOP</p>', unsafe_allow_html=True)
                     
                    with col113:
                        st.write("TPH")
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">3.500</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;">0</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">4.000</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;">0</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">2.500</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;">0</p>', unsafe_allow_html=True)
                    col1111,col1112 = st.columns([7,14])
                    with col1111:
                        st.markdown(f'<p style=text-align:left;font-size:12px;border-radius:2%;">COAL QUALITY</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style=text-align:left;font-size:12px;border-radius:2%;">DESTINATION</p>', unsafe_allow_html=True)
                    with col1112:
                        st.markdown(f'<p style="background-color:white;color:black;text-align:left;font-size:12px;border-radius:2%;">MELAWAN</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:black;text-align:left;font-size:12px;border-radius:2%;">PORT</p>', unsafe_allow_html=True)
        with col11:
            with st.container(border=True):
                st.markdown(f'<p style="background-color:black;text-align:center;font-size:20px;border-radius:2%;">STREAM2</p>', unsafe_allow_html=True)
                with st.container():
                    col111_2,col112_2,col113_2 = st.columns([7,7,7])
                    with col111_2:
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;"></p><br>', unsafe_allow_html=True)
                        st.markdown(f'<p style=text-align:left;font-size:12px;border-radius:2%;">CV06</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;">CV08</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;">OLC-2</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;">STOCKPILE TC</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;">STACKING</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;">RECLAIMING</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;">MTC</p>', unsafe_allow_html=True)
                    with col112_2:
                        st.write("STATUS")
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">RUN</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;">STOP</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">RUN</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;">STOP</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">RUN</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;">STOP</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">RUN</p>', unsafe_allow_html=True)
                     
                    with col113_2:
                        st.write("TPH")
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">3.500</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;">0</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">4.000</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;"></p><br>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">2.500</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;">0</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;"></p><br>', unsafe_allow_html=True)
                     
                    col11_21,col11_22 = st.columns([7,14])
                    with col11_21:
                        st.markdown(f'<p style=text-align:left;font-size:12px;border-radius:2%;">SURGE BIN LEVEL</p>', unsafe_allow_html=True)
                    with col11_22:
                        st.markdown(f'<p style="background-color:white;color:black;text-align:left;font-size:12px;border-radius:2%;">30%</p>', unsafe_allow_html=True)
        with col12:
            with st.container(border=True):
                st.markdown(f'<p style="background-color:black;text-align:center;font-size:20px;border-radius:2%;">SHIP LOADING FACILITY</p>', unsafe_allow_html=True)
                with st.container():
                    col121,col122,col123 = st.columns([7,7,7])
                    with col121:
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;"></p><br>', unsafe_allow_html=True)
                        st.markdown(f'<p style=text-align:left;font-size:12px;border-radius:2%;">TRESTLE</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;">SOUTH TC</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;">SOUTH SL</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;">NORTH TC</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;">NORTH SL</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;"></p><br>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;"></p><br>', unsafe_allow_html=True)
                    with col122:
                        st.write("STATUS")
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">RUN</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;">STOP</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">RUN</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;">STOP</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">RUN</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;"></p><br>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;"></p><br>', unsafe_allow_html=True)
                    with col123:
                        st.write("TPH")
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">3.500</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;">0</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:11px;border-radius:2%;"></p><br>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;">2.500</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;"></p><br>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;"></p><br>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;"></p><br>', unsafe_allow_html=True)
        with col12:
            with st.container(border=True):
                st.markdown(f'<p style="background-color:black;text-align:center;font-size:20px;border-radius:2%;">BARGE LOADING FACILITY</p>', unsafe_allow_html=True)
                with st.container():
                    col121_2,col122_2,col123_2 = st.columns([7,7,7])
                    with col121_2:
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;"></p><br>', unsafe_allow_html=True)
                        st.markdown(f'<p style=text-align:left;font-size:12px;border-radius:2%;">BTC-1</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;">BTC-2</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="text-align:left;font-size:12px;border-radius:2%;">BLC</p>', unsafe_allow_html=True)
                    with col122_2:
                        st.write("STATUS")
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">RUN</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;">STOP</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">RUN</p>', unsafe_allow_html=True)
                       
                    with col123_2:
                        st.write("TPH")
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;"></p><br>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;"></p><br>', unsafe_allow_html=True)
                        st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:11px;border-radius:2%;">2.500</p>', unsafe_allow_html=True)
                   
                       
                    col12_21,col12_22 = st.columns([7,14])
                    with col12_21:
                        st.markdown(f'<p style=text-align:left;font-size:12px;border-radius:2%;">TOTALIZER</p>', unsafe_allow_html=True)
                        st.markdown(f'<p style=text-align:left;font-size:12px;border-radius:2%;">WIN SPEED</p>', unsafe_allow_html=True)
                    with col12_22:
                        st.markdown(f'<p style="background-color:white;color:black;text-align:left;font-size:12px;border-radius:2%;">2.500 TONNES</p>', unsafe_allow_html=True)        
                        st.markdown(f'<p style="background-color:white;color:black;text-align:left;font-size:12px;border-radius:2%;">3 KNOTS</p>', unsafe_allow_html=True)        

with col2:
    with st.container(border=True):
        st.markdown(f'<p style="background-color:black;text-align:center;font-size:24px;border-radius:2%;">BENGALON</p>', unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown(f'<p style="background-color:black;text-align:center;font-size:20px;border-radius:2%;">BARGE LOADING FACILITY</p>', unsafe_allow_html=True)
            with st.container():
                col211,col212,col213 = st.columns([7,7,7])
                with col211:
                    st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;"></p><br>', unsafe_allow_html=True)
                    st.markdown(f'<p style=text-align:left;font-size:12px;border-radius:2%;">CV01-INLOADING</p>', unsafe_allow_html=True)
                    st.markdown(f'<p style=text-align:left;font-size:12px;border-radius:2%;">CV05-OUTLOADING</p>', unsafe_allow_html=True)
                with col212:
                    st.write("STATUS")
                    st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">RUN</p>', unsafe_allow_html=True)     
                    st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;">STOP</p>', unsafe_allow_html=True)     
                with col213:
                    st.write("TPH")
                    st.markdown(f'<p style="background-color:white;color:red;text-align:left;font-size:12px;border-radius:2%;">3.500</p>', unsafe_allow_html=True)
                    st.markdown(f'<p style="background-color:white;color:green;text-align:left;font-size:12px;border-radius:2%;">0</p>', unsafe_allow_html=True)
                   