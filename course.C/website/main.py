import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv")

st.header("The Mike B Study Website")
company_desc = """
A person that studies to produce projects that work well. There are actually no employees, but 
the project involves producing a company web site with employees. I have a set of pictures so,  
I'm pretending I have a team.
"""
st.write(company_desc)

st.subheader("The Team")

row_count = len(df)
# st.write(row_count)
col1_rows = int(row_count / 3)
if row_count % 3 >= 1:
    col1_rows += 1
col2_rows = int(row_count / 3) + col1_rows
if row_count % 3 >= 2:
    col2_rows += 1

# Produces uniform columns and info in the boxes within the columns.
col1, col2, col3 = st.columns(3)
# Does not work as well. Adds extra space after Persons name in some cases.
#col1, space1, col2, space2, col3 = st.columns([1.25, 0.25, 1.25, 0.25, 1.25])

with col1:
    for idx, row in df[:col1_rows].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image("images/"+row['image'])
        # Provide a little more space at the bottom of the box for separation
        st.write("&nbsp;")

with col2:
    for idx, row in df[col1_rows:col2_rows].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image("images/"+row['image'])
        st.write("&nbsp;")

with col3:
    for idx, row in df[col2_rows:].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image("images/"+row['image'])
        st.write("&nbsp;")
