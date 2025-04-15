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
#col3, spacer_col, col4 = st.columns([2,0.125,2])
col3, col4 = st.columns(2)

display_idx = 0
for idx, row in df.iterrows():
    if display_entry(row["status"]):
        column = col3 if display_idx % 2 == 0 else col4
        display_idx += 1
        with column:
            column.subheader(row["title"])
            column.write(row["description"])
            column.write(f"Status: &nbsp;&nbsp;**{row['status']}**")
            column.image("images/"+row["image"])
            if row["status"] == "Not Started" or row["status"] == "Started" :
                #column.markdown(f"Status: &nbsp;&nbsp;**{row['status']}**")
                pass
            else:
                #column.markdown(f"Status: &nbsp;&nbsp;**{row['status']}** {spacer} [Source Code]({row['url']})")
                column.markdown(f"[Source Code]({row['url']})")
            #column.markdown(f"<div align='center'>[Source Code]({row['url']})</div>",unsafe_allow_html=True)
            #source_code = f"[Source Code]({row['url']})"
            #column.markdown(f"""<div align='center'>{source_code}</div>""",unsafe_allow_html=True)
            #column.write(f"[Source Code]({row['url']})")

