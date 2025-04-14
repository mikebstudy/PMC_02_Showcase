import streamlit as st

# Data structure
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
    }
]

# App title
st.title("Project Showcase")

# Create two columns
col1, col2 = st.columns(2)

# Loop through projects and alternate columns
for i, project in enumerate(projects):
    with col1 if i % 2 == 0 else col2:  # Alternate between columns
        st.subheader(project["title"])
        st.write(f"**Status:** {project['status']}")
        st.write(f"**Description:** {project['description']}")
        st.write(f"[Visit here]({project['url']})")

        # Display image if available
        if project["image"]:
            st.image("images/"+project["image"], caption=project["title"], use_column_width=True)

        st.write("---")  # Divider between projects
