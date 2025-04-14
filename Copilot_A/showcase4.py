import streamlit as st

# Data structure
# Updated data structure
projects = [
    {
        "title": "Todo App",
        "status": "Done",
        "description": "A distraction-free web app to help you focus on creating and completing tasks.",
        "url": "https://github.com/mikebstudy/PMC_01_ToDoList.git",
        "image": "1.png"
    },
    {
        "title": "Portfolio Website",
        "status": "Doing Extra",
        "description": "A website built entirely in Python to showcase coding projects and apps.",
        "url": "https://pythonhow.com",
        "image": "2.png"
    },
    {
        "title": "PDF Templates",
        "status": "Started",
        "description": "A script that generates PDF templates of multiple pages given some predefined guidelines.",
        "url": "https://pythonhow.com",
        "image": "3.png"
    },
    {
        "title": "PDF Invoices",
        "status": "Not Started",
        "description": "A script that reads invoice records from Excel files and automatically generates PDF invoices.",
        "url": "https://pythonhow.com",
        "image": "4.png"
    },
    {
        "title": "Positive News Site",
        "status": "Not Started",
        "description": "A website that gets data from a news API and uses sentiment analysis to publish only positive news.",
        "url": "https://pythonhow.com",
        "image": "5.png"
    }
]

# App title
st.title("Project Showcase")

# Checkbox filters
statuses = sorted(list(set(project["status"] for project in projects)))
selected_statuses = []

st.write("### Filter by status:")
for status in statuses:
    if st.checkbox(status, value=True):  # Default to all checkboxes being checked
        selected_statuses.append(status)

# Filter projects based on selected statuses
filtered_projects = [
    project for project in projects
    if not selected_statuses or project["status"] in selected_statuses
]

# Two-column layout for displaying projects
col1, col2 = st.columns(2)

# Display filtered projects
for i, project in enumerate(filtered_projects):
    column = col1 if i % 2 == 0 else col2
    with column:
        st.subheader(project["title"])
        st.write(f"**Status:** {project['status']}")
        st.write(f"**Description:** {project['description']}")
        st.write(f"[Visit here]({project['url']})")

        # Display image if available
        if project["image"]:
            st.image("images/" + project["image"], caption=project["title"], use_column_width=True)

        st.write("---")  # Divider between projects
