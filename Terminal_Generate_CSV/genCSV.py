import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.add_vertical_space import add_vertical_space
import streamlit_nested_layout

st.set_page_config(layout="wide")
col1,col2,col3 = st.columns(3)
with col1:
    with stylable_container(
        key="cat_container1",
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
                """,
                """
                button {
                    border: solid .3em #292746;
                    border-radius: 20px;
                    color: #fff;
                    background-color: #000;
                }
                """,
                """
                button:hover {
                     background-color: red;
                }
                """,
                ],
        ):
            col11,col12,col13 = st.columns([5,20,5])
            with col12:
                st.markdown(f'<p style="background-color:black;text-align:center;font-size:30px;border-radius:2%;">SHIFT REPORTING</p>', unsafe_allow_html=True)
            col1_1, col1_2, col1_3,col1_4 = st.columns([4,11,11,4]) 
            with col1_2:
                st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">SHIFT REPORTING:</p>', unsafe_allow_html=True)
                add_vertical_space(1)
                st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">DATE:</p>', unsafe_allow_html=True)
                add_vertical_space(1)
                st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">TIME:</p>', unsafe_allow_html=True)
                add_vertical_space(1)
                st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">PATH DIRECTORY:</p>', unsafe_allow_html=True)
            # Add a select box in the second column
            with col1_3:
                option1 = st.selectbox(
                    '',
                    ('Option 1', 'Option 2', 'Option 3'),key="option1",label_visibility="collapsed"
                )  
                option2 = st.selectbox(
                    '',
                    ('Option 1', 'Option 2', 'Option 3'),key="option2",label_visibility="collapsed"
                )
                option3 = st.selectbox(
                    '',
                    ('Option 1', 'Option 2', 'Option 3'),key="option3",label_visibility="collapsed"
                )  
                option4 = st.selectbox(
                    '',
                    ('Option 1', 'Option 2', 'Option 3'),key="option4",label_visibility="collapsed"
                )
            col11_2,col12_2,col13_2 = st.columns([12,6,12])    
            with col12_2:
                 st.button("Generate",key="button1")
with col2:           
    with stylable_container(
            key="cat_container1",
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
                """,
                """
                button {
                    border: solid .3em #292746;
                    border-radius: 20px;
                    color: #fff;
                    background-color: #000;
                }
                """,
                """
                button:hover {
                     background-color: red;
                }
                """,
                ],

        ):
            col21,col22,col23 = st.columns([5,20,5])
            with col22:
                st.markdown(f'<p style="background-color:black;text-align:center;font-size:30px;border-radius:2%;">TRENDING</p>', unsafe_allow_html=True)
            col2_1, col2_2, col2_3,col2_4 = st.columns([4,11,11,4]) 
            with col2_2:
                st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">GROUP:</p>', unsafe_allow_html=True)
                add_vertical_space(1)
                st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">DATE:</p>', unsafe_allow_html=True)
                add_vertical_space(1)
                st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">SHIFT:</p>', unsafe_allow_html=True)
                add_vertical_space(1)
                st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">PATH DIRECTORY:</p>', unsafe_allow_html=True)
            # Add a select box in the second column
            with col2_3:
                option21 = st.selectbox(
                    '',
                    ('Option 1', 'Option 2', 'Option 3'),key="option21",label_visibility="collapsed"
                )  
                option22 = st.selectbox(
                    '',
                    ('Option 1', 'Option 2', 'Option 3'),key="option22",label_visibility="collapsed"
                )
                option23 = st.selectbox(
                    '',
                    ('Option 1', 'Option 2', 'Option 3'),key="option23",label_visibility="collapsed"
                )  
                option24 = st.selectbox(
                    '',
                    ('Option 1', 'Option 2', 'Option 3'),key="option24",label_visibility="collapsed"
                )
            col21_2,col22_2,col23_2 = st.columns([12,6,12])    
            with col22_2:
                 st.button("Generate",key="button2")
with col3:
    with stylable_container(
            key="cat_container1",
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
                """,
                """
                button {
                    border: solid .3em #292746;
                    border-radius: 20px;
                    color: #fff;
                    background-color: #000;
                }
                """,
                """
                button:hover {
                     background-color: red;
                }
                """,
                ],
        ):
            col31,col32,col33 = st.columns([5,20,5])
            with col32:
                st.markdown(f'<p style="background-color:black;text-align:center;font-size:30px;border-radius:2%;">VESSEL REPORTING</p>', unsafe_allow_html=True)
            col3_1, col3_2, col3_3,col3_4 = st.columns([4,11,11,4]) 
            with col3_2:
                st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">VESSEL NAME:</p>', unsafe_allow_html=True)
                add_vertical_space(1)
                st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">PATH DIRECTORY:</p>', unsafe_allow_html=True)
                # Add a select box in the second column
            with col3_3:
                option31 = st.selectbox(
                    '',
                    ('Option 1', 'Option 2', 'Option 3'),key="option31",label_visibility="collapsed"
                )  
                option32 = st.selectbox(
                    '',
                    ('Option 1', 'Option 2', 'Option 3'),key="option32",label_visibility="collapsed"
                )
            col31_2,col32_2,col33_2 = st.columns([12,6,12])    
            with col32_2:
                 add_vertical_space(7)
                 st.button("Generate",key="button3")