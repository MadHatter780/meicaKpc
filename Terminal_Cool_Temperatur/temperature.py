import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(layout="wide")
st.header("COAL TERMINAL-COAL TEMPERATURE")


col1,col2 = st.columns(2)
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
                """
                ],
            ):

                        col2_1, col2_2, col2_3,col2_4 = st.columns([7,11,11,7]) 
                        with col2_2:
                            st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">CV-03 Coal:</p>', unsafe_allow_html=True)
                            add_vertical_space(1)
                            st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">CV-04 Coal</p>', unsafe_allow_html=True)
                            add_vertical_space(1)
                            st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">OLC Coal:</p>', unsafe_allow_html=True)
                            add_vertical_space(1)
                            st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">Stacker Reclaimer Coal:</p>', unsafe_allow_html=True)
                            add_vertical_space(1)
                            st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">South Transfer Coal:</p>', unsafe_allow_html=True)
                            add_vertical_space(1)
                            st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">North Transfer Coal:</p>', unsafe_allow_html=True)
                            add_vertical_space(1)
                            st.markdown(f'<p style="margin-bottom:6px;text-align:left;font-size:20px;border-radius:2%;">BLF Coal:</p>', unsafe_allow_html=True)
       
                            # Add a select box in the second column
                        with col2_3:
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
                            option5 = st.selectbox(
                            '',
                                ('Option 1', 'Option 2', 'Option 3'),key="option5",label_visibility="collapsed"
                            )
                            option6 = st.selectbox(
                            '',
                                ('Option 1', 'Option 2', 'Option 3'),key="option6",label_visibility="collapsed"
                            )  
                            option7 = st.selectbox(
                            '',
                                ('Option 1', 'Option 2', 'Option 3'),key="option7",label_visibility="collapsed"
                            )