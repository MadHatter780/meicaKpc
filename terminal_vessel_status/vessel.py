import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.add_vertical_space import add_vertical_space


st.set_page_config(layout="wide")
st.title("Coal Terminal-Vessel Status")

#expander with image
with st.container(border=True):
        
    #layout 2x2 column

        col1,col2 = st.columns(2)
        with col1:
            with stylable_container(
                key="cat_container1",
                    css_styles=[
                    """
                {
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
                Vc1, Vc2, Vc3 = st.columns([1,5,1])
                with Vc2:
                    Vvariable_output1 = "CARALOS GLORY"
                    Vvariable_output2 = "03 March 2024"
                    Vvariable_output3 = "11:00:20"
                    font_size = 20
                    html_str = f"""
                    <style>
                        p.a {{
                        font: bold {font_size}px Courier;
                        background-color: black;
                        }}
                    </style>
                    <p class="a">LOADING RATE : {Vvariable_output1}</p>
                    <p class="a">COMPLETION DATE : {Vvariable_output2}</p>
                    <p class="a">COMPLETION TIME : {Vvariable_output3}</p>
                    """
                    st.markdown(
                        html_str,unsafe_allow_html=True)

        with col1:
            with stylable_container(
                key="cat_container2",
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
                Tc1, Tc2, Tc3 = st.columns([1,5,1])
                with Tc2:
                    st.header(":red[Target]")
                    Tvariable_output1 = "5.200 TPH"
                    Tvariable_output2 = "05 March 2024"
                    Tvariable_output3 = "16:00:11"
                    font_size = 20
                    html_str = f"""
                    <style>
                        p.a {{
                        font: bold {font_size}px Courier;
                        background-color: black;
                    }}
                    </style>
                    <p class="a">LOADING RATE : {Tvariable_output1}</p>
                    <p class="a">COMPLETION DATE : {Tvariable_output2}</p>
                    <p class="a">COMPLETION TIME : {Tvariable_output3}</p>
                    """
                    st.markdown(
                        html_str,unsafe_allow_html=True)

        with col2:
            add_vertical_space(8)

        with col2:  
            with stylable_container(
                key="cat_container3",
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
                Ac1, Ac2, Ac3 = st.columns([1,5,1])
                with Ac2:
                    st.header(":green[Actual Updated]")
                    variable_output1 = "4.200 TPH"
                    variable_output2 = "06 March 2024"
                    variable_output2 = "08:00:50"
                    font_size = 20
                    html_str = f"""
                    <style>
                        p.a {{
                        font: bold {font_size}px Courier;
                        background-color: black;
                        }}
                    </style>
                    <p class="a">AVG LOADING RATE: {variable_output1}</p>
                    <p class="a">EST. COMPLETION DATE : {variable_output2}</p>
                    <p class="a">EST. COMPLETION TIME : {variable_output2}</p>
                    """
                    st.markdown(
                        html_str,unsafe_allow_html=True)

with st.container(border=True):
    col1,col2,col3=st.columns(3)
    with col1:
        st.write("TOTAL CAPACITY = 79.665 TONES")
    with col2:
        st.write("TOTAL CAPACITY = 79.665 TONES")
    with col3:
        st.write("TOTAL CAPACITY = 79.665 TONES")