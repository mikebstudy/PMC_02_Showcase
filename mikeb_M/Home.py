import streamlit as st
import pandas as pd

df = pd.read_csv( "data.csv", sep=";")

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/mikebstudy.png")

with col2:
    st.title("Mike Brennan")
    content="""
    Hi, this is **Mike Brennan** studying Python by working through the Python Mega Course 
    *(offered on Udemy by Ardit Sulce)*. I've been a **software developer** for many years, but I'm new to Python.
    I'm using this course to come up to speed and develop sufficient skills to work as a **Python developer**.
    """
    st.markdown(content)

content2 = """
The approach I'm taking in working through the course is three fold - for each course project:  \n
1. Do the project, &nbsp;&nbsp;&nbsp;&nbsp; 2. Enhance the project, &nbsp;&nbsp;&nbsp;&nbsp; 3. Test an AI chatbot's ability to do the project.  \n 
There are 20 projects in the course.
"""
st.markdown(content2)

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

