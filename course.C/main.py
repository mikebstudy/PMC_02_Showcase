import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/mikebstudy.png")

with col2:
    st.title("mikebstudy")
    content="""
    Hi, this is 'mikebstudy' working through the Python Mega Course. There are 20 projects. So far I've completed
    the first project and am working on the second project, this Showcase project. The picture is of the author of the 
    course, not me.
    """
    st.info(content)
