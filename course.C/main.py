import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/mikebstudy.png")

with col2:
    st.title("mikebstudy")
    content="""
    Hi, this is 'mikebstudy' working through the Python Mega Course. There are 20 projects. 
    """
    st.info(content)

content2 = """
Below are the apps that are part of the course work. I've only built the first one, but the others are coming.
"""
st.write(content2)