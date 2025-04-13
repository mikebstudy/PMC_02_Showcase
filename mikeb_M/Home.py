import streamlit as st
import pandas as pd

df = pd.read_csv( "data.csv", sep=";")

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/mikebstudy.png")

with col2:
    st.title("Mike B Study")
    content="""
    Hi, this is 'mikebstudy' working through the Python Mega Course. There are 20 projects. 
    """
    st.info(content)

content2 = """
Below are the apps that are part of the course work. I've only built the first one, but the others are coming.
"""
st.write(content2)

#cbx1, cbx2, cbx3, cbx4 = st.columns(4)

#with cbx1:
    #st.markdown("*Status*")
    #st.subheader("Status")
st.markdown("**Status**")

#with cbx2:
done = st.checkbox("Done", value=True)

#with cbx3:
in_progress = st.checkbox('In Progress', value=True)

#with cbx4:
not_started = st.checkbox('Not Started', value=False)

def display_entry(status):
    if not_started and status=="Not Started":
        return True
    if done and status=="Done":
        return True
    if in_progress and status!="Not Started" and status!="Done":
        return True
    return False

spacer = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
col3, spacer_col, col4 = st.columns([2,0.125,2])

with col3:
    for idx, row in df[:10].iterrows():
        if display_entry(row['status']):
            st.subheader(row["title"])
            st.write(row["description"])
            st.image("images/"+row["image"])
            if row["status"] == "Not Started" or row["status"] == "Started" :
                st.markdown(f"Status: &nbsp;&nbsp;**{row['status']}**")
            else:
                st.markdown(f"Status: &nbsp;&nbsp;**{row['status']}** {spacer} [Source Code]({row['url']})")

with col4:
    for idx, row in df[10:].iterrows():
        if display_entry(row['status']):
            st.subheader(row["title"])
            st.write(row["description"])
            st.image("images/"+row["image"])
            if row["status"] == "Not Started" or row["status"] == "Started" :
                st.markdown(f"Status: &nbsp;&nbsp;**{row['status']}**")
            else:
                st.markdown(f"Status: &nbsp;&nbsp;**{row['status']}** {spacer} [Source Code]({row['url']})")

