import streamlit as st
import pandas as pd

df = pd.read_csv( "data.csv", sep=";")

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

col3, spacer_col, col4 = st.columns([1.5,0.5,1.5])

with col3:
    for idx, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for idx, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

